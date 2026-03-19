# Employee Management System

This project is a **Command Line Employee Management System** built using Python and Object-Oriented Programming (OOP).
It allows users to manage employee information such as adding, viewing, searching, updating, and deleting employee records.

## Features

* Add new employee
* Show all employees in table format
* Search employee by ID
* Update employee information
* Delete employee record
* Input validation for salary and email
* Private salary attribute for better data protection

## Technologies Used

* Python
* Object-Oriented Programming (Classes & Objects)
* `tabulate` library (for table display)
* Exception Handling

## Menu Options

```id="menuemp"
1. Add Employee
2. Show All Employees
3. Search Employee by ID
4. Delete Employee by ID
5. Update Employee
6. Exit
```

## Example Output

Employees are displayed in a table format:

```id="tableemp"
+----+---------+------------+----------+--------+-----------+-------------------+
| ID | Name    | Department | Position | Salary | Phone     | Email             |
+----+---------+------------+----------+--------+-----------+-------------------+
|101 | Rakib   | IT         | Manager  | 50000  | 017xxxxxx |  rakib@email.com  |
+----+---------+------------+----------+--------+-----------+-------------------+
```

## How to Run

1. Install required library:

```id="installemp"
pip install tabulate
```

2. Run the program:

```id="runemp"
python office-management-system.py
```

## Concepts Used

* Classes and Objects
* Encapsulation (`__salary` private attribute)
* Loops and Conditions
* Exception Handling
* List Data Storage

## Author

Sabbir Khan
