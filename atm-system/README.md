# ATM System (Bank Account Simulation)

This project is a simple **ATM / Bank Account Simulation System** built using Python and Object-Oriented Programming (OOP).
It allows users to perform basic banking operations such as deposit, withdraw, and check account balance using a PIN.

## Features

* Create a bank account
* Deposit money
* Withdraw money with PIN verification
* Check account balance
* Private PIN security using encapsulation
* Withdrawal rules for ATM simulation

## Withdrawal Rules

* Maximum withdrawal limit: **20,000 Taka**
* Withdrawal amount must be in **500 or 1000 note multiples**
* Cannot withdraw more than available balance
* PIN verification required

## Technologies Used

* Python
* Object-Oriented Programming (Classes & Objects)
* Encapsulation (Private variables and methods)

## Example Usage

```id="atmexample"
b1 = BankAccount("Tuhin", 50000, 4625)

b1.deposit(10000)
b1.withdraw(3000, 4625)

b1.check_blance(4625)

b1.withdraw(3232, 4625)
```

## Example Output

```id="atmoutput"
Deposit successful Balance: 60000
Withdraw successful balance 57000
Available Balance: 57000
You can withdraw only 500 & 1000 notes
```

## Concepts Used

* Classes and Objects
* Private attributes (`__pin`)
* Private methods (`__check_pin`)
* Conditional statements
* Basic banking logic

## Author

Sabbir Khan
