__author__ = "ACE Faculty"
__version__ = "1.16.8"
__credits__ = "Cherub Meracap"

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    Represents a window that provides the UI to manage Clients
    """

    def __init__(self):
        """
        Initializes a new instance of ClientLookupWindow class
        """
        self.__client_listing = load_data()[0]
        self.__accounts = load_data()[1]
        super().__init__()
        self.lookup_button.clicked.connect(self.__on_lookup_client)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.account_table.cellClicked.connect(self.__on_select_account)
        self.filter_button.clicked.connect(self.__on_filter_clicked)

    @Slot() 
    def __on_lookup_client(self):
        """
        Function that act as a slot for 
        lookup_button_clicked signal
        """
        try:
            client_number = int(self.client_number_edit.text())
        except ValueError:
            QMessageBox.critical(
                self, 
                "Input Error",
                "The client number must be a numeric value.",
                QMessageBox.Ok
            )
            self.reset_display()
            return
        
        if client_number not in self.__client_listing:
            QMessageBox.critical(
                self,
                "Not Found",
                f"Client number: {client_number} not found",
                QMessageBox.Ok
            )
            self.reset_display()
            return
        else:
            first_name = self.__client_listing[client_number].first_name
            last_name = self.__client_listing[client_number].last_name
            self.client_info_label.setText(f"Client Name: {first_name} {last_name}")
            self.__toggle_filter(False)

            for account in self.__accounts.values():
                if account.client_number == client_number:
                    row = self.account_table.rowCount()
                    self.account_table.insertRow(row)

                    account_number = QTableWidgetItem(str(account.account_number))
                    balance = QTableWidgetItem(f"${account.balance:,.2f}")
                    date_created = QTableWidgetItem(str(account._date_created))
                    account_type = QTableWidgetItem(account.__class__.__name__)

                    account_number.setTextAlignment(Qt.AlignCenter)
                    balance.setTextAlignment(Qt.AlignRight)
                    date_created.setTextAlignment(Qt.AlignCenter)
                    account_type.setTextAlignment(Qt.AlignCenter)

                    self.account_table.setItem(row, 0, account_number)
                    self.account_table.setItem(row, 1, balance)
                    self.account_table.setItem(row, 2, date_created)
                    self.account_table.setItem(row, 3, account_type)

                    self.account_table.resizeColumnsToContents()

    @Slot()
    def __on_text_changed(self):
        """
        Function to act as a slot for 
        client_number_edit textChanged signal
        to clear all bank account records from account_table
        """
        self.account_table.setRowCount(0)

    @Slot(int, int)
    def __on_select_account(self, row: int, column: int) -> None:
        """
        Function to act as a slot for
        account_table cellClicked signal
        """
        
        account_number_picked = self.account_table.item(row, 0)
        account_number = int(account_number_picked.text())

        if not account_number or account_number == 0:
            QMessageBox.critical(
                    self,
                    "Invalid Selection",
                    "Please select a valid record.",
                    QMessageBox.Ok
                )
            return
        
        if account_number in self.__accounts:
            bank_account = self.__accounts.get(account_number)
            account_detail = AccountDetailsWindow(bank_account)
            account_detail.balance_update.connect(self.update_data)
            account_detail.exec_()
        else:
            QMessageBox.critical(
                self,
                "No Bank Account",
                "Bank Account selected does not exist.",
                QMessageBox.Ok
            )

    @Slot(BankAccount)
    def update_data(self, account: BankAccount) -> None:
        """
        Method that acts as slot for balance_updated signal
        Args:
            account: The BankAccount object being updated
        Returns:
            None
        """
        for row in range(self.account_table.rowCount()):
            account_num_table = self.account_table.item(row, 0).text()

            if int(account_num_table) == account.account_number:
                table_balance = self.account_table.item(row, 1)

                table_balance.setText(f"${account.balance:,.2f}")

                self.__accounts[account.account_number] = account

                update_data(account)
                break

    @Slot()
    def __on_filter_clicked(self):
        """
        Method that acts as slot for filter_button clicked signal
        Args:
            None
        Returns:
            None
        """
        filter_button_text = self.filter_button.text()
        if filter_button_text != "Apply Filter":
            self.__toggle_filter(False)
        else:
            filter_combo_box_index = self.filter_combo_box.currentIndex()
            filter_edit_text = self.filter_edit.text().lower()
            self.__toggle_filter(True)

            for row in range(self.account_table.rowCount()):
                row_data = self.account_table.item(row, filter_combo_box_index)

                if row_data and filter_edit_text in row_data.text().lower():
                    self.account_table.setRowHidden(row, False)
                else:
                    self.account_table.setRowHidden(row, True)

    def __toggle_filter(self, filter_on: bool) -> None:
        """
        Method to toggle the display of filter widgets to
        indicate to user wheter filtering is taking place
        Args:
            filter_on(Boolean): Indicates whether filtering 
                                is taking place
        Returns:
            None
        """
        self.filter_button.setEnabled(True)

        if filter_on == True:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setDisabled(True)
            self.filter_edit.setDisabled(True)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)
            
            self.filter_label.setText("Data is Not Currently Filtered")

