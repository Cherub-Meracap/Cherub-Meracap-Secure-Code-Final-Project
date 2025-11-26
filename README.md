# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Cherub Meracap

## Assignment
Assignment 1: Classes, Encapsulation and Unit Test Planning
Assignment 2: Abstraction, Inheritance and Polymorphism
Assignment 3: Design Patterns
Assignment 4: Programming Paradigms
Assignment 5: Algorithms, Help Files and Distribution

## Encapsulation
Encapsulation was achieved in the BankAccount class by having the attributes of the BankAccount private thorugh double underscore. Another part of the encapsulation is having accessor methods so that reading of the private attributes can be controlled, another is update_balance, deposit, and withdraw methods makes sure that validation is applied before changing the value of balance. 

Another part is public methods interact with the private attribute allowing for the ability to use specific operations while applying validation to it. Another part of encapsulation is the str method which makes sure that it provides a controlled way of displaying sensitive information on the BankAccount class.

## Polymorphism
Polymorphism in this assignment was achived through inheritance and abstraction, first the get_service_charge method was abstracted to be able to be overriden by get_service_charge methods in the subclasses. The abstracted get_service_charge method is then inherited by each of the subclasses to be implemented based on each of the subclasses' operations.

## Strategy Pattern
The strategy Pattern is being used in this assignment to consolidate
the get service charge function to one place. Instead of having 
multiple different get_service_charge function on different bank account python files it is now inside a strategy pattern python file.
It also you to being to modify the get_service_charge function without having to modify each bank account file making it easier to maintain and reuse the code.

## Observer pattern
The observer pattern is being used in this assignment to observe different subjects
which are the multiple types of bank accounts such as chequing, savings, and investment
accounts. The observer strategy also notifies the client about any potention anoymalous behaviours in their bank accounts for example high transaction amount or low balance. 
It is able to do that via the notify method and the update method which notifies 
observers of a state change and sends out a message in the form of an email.

## Event-Driven Programming Paradigm 
This paradigm was implemented in this application via Pyside6's slots and signal. A GUI was implemented to take in user input which was then captured as a signal and methods such as on_select_account, on_lookup_client, etc are defined in order to respond to the user input which are called as slots which is an event handler for a specific type of event for example on_lookup_client is a slot for the lookup button being clicked event which is a user clicking the button after putting a specific client number.

## Filtering
Filtering was incorporated in this assignment via the search text
on the application that aims to filter data based on 4 categories:
Account number, balance, Date created and Account Type.
Data was filtered by iterating over all the rows and using an if
statement to check if that row has the value of what the user is 
searching.