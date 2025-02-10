# Password Cracker

This is a simple Python script for cracking passwords using brute force. The script generates all possible combinations of characters and tries to match the target password.

## Features

- It uses brute-force to check every possible password combination.
- The password length can vary from 1 to 8 characters.
- It works with lowercase, uppercase, digits, and punctuation characters.

## How It Works

1. The script generates possible combinations using the `itertools.product` function.
2. It tries every combination of characters in a loop, checking if the current combination matches the target password.
3. If it finds a match, it prints the password and stops.

## Requirements

- Python 3.x
- No external libraries required, only standard Python libraries (`itertools`, `string`).

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/password-cracker.git
