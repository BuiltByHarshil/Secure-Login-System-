# Secure Login System

This project implements a Secure Login System in Python that allows users to register, log in, and reset their passwords using email-based authentication. User passwords are securely stored using SHA-256 hashing.

## Features
- User registration
- User login authentication
- Forgot password / password reset
- Email format validation
- Strong password validation
- Password hashing using SHA-256
- Local file-based storage (users.txt)

## Tech Stack
- Python
- hashlib
- re
- os

## How It Works
- Passwords are never stored in plain text.
- During registration, passwords are hashed before saving.
- During login, the entered password is hashed and compared with the stored hash.
- Password reset updates the stored hash for the user.

## How to Run
1. Make sure Python is installed.
2. Run the script:
   python main.py

## File Storage
User credentials are stored in a local file named users.txt.

## Notes
This is a basic implementation for learning purposes and is not intended for production use.
