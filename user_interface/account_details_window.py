__author__ = "ACE Faculty"
__version__ = "1.4.1"
__credits__ = "Cherub Meracap"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, Slot
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    # Signal
    balance_update = Signal(BankAccount)
    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        super().__init__()
        if isinstance(account, BankAccount):
            self.__account = copy.copy(account)

            self.account_number_label.setText(str(self.__account.account_number))
            self.balance_label.setText(f"${self.__account.balance:,.2f}")
            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            self.reject()

    @Slot()
    def __on_apply_transaction(self):
        """
        Method will act as a slot for the
        deposit_button and withdraw_button signals
        to perform a transaction using the amount entered.
        Args:
            None
        Returns:
            None
        """
        try:
            amount = float(self.transaction_amount_edit.text())
        except ValueError:
            QMessageBox.critical(
                self, 
                "Invalid Amount",
                "Amount must be numeric.",
                QMessageBox.Ok
            )
            self.transaction_amount_edit.setFocus()
            return
        
        try:
            button_clicked = self.sender()
            
            if button_clicked == self.deposit_button:
                transaction_type = "Deposit"
                self.__account.deposit(amount)

            if button_clicked == self.withdraw_button:
                transaction_type = "Withdraw"
                self.__account.withdraw(amount)
            self.balance_update.emit(self.__account)

            self.balance_label.setText(f"{self.__account.balance:,.2f}")
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()
            
        except Exception as e:
            QMessageBox.critical(
                self, 
                f"{transaction_type} Failed",
                f"{e}",
                QMessageBox.Ok
            )
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

    @Slot()
    def __on_exit(self):
        """
        Method to act as a slot for exit_button clicked signal
        Args:
            None
        Returns:
            None
        """
        self.close()
