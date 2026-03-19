# Password Generator

This project is a simple **Password Generator** built with Python.
It generates a random password based on the length provided by the user.

## Features

* Generate strong random passwords
* User can choose password length
* Uses letters, numbers, and symbols
* Option to generate numeric-only passwords

## Technologies Used

* Python
* `random` module
* `string` module

## How It Works

1. The program asks the user to enter the password length.
2. It combines:

   * uppercase and lowercase letters
   * digits
   * special characters
3. A random password is generated using `random.choice()`.

Example input:

```id="ex1pw"
Enter your password length: 10
```

Example output:

```id="ex2pw"
Generated Password: A@3kP!9xQ2
```

## Numeric Password Generator

The project also includes a function to generate **number-only passwords**, useful for OTP or PIN codes.

Example:

```id="ex3pw"
Number password: 483920
```

## Author

Sabbir Khan
