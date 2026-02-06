import hashlib
import re
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def email_exists(email):
    if not os.path.exists("users.txt"):
        return False

    with open("users.txt", "r") as file:
        for line in file:
            stored_email = line.split(":")[0].strip().lower()
            if stored_email == email:
                return True
    return False


def is_valid_email(email):
    return re.search(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)


def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True


def register():
    print("\nEmail Registration")

    email = input("Enter email: ").strip().lower()

    if not is_valid_email(email):
        print("Invalid email format")
        return

    if email_exists(email):
        print("Email already registered")
        return

    print("\nPassword must contain:")
    print("- Minimum 8 characters")
    print("- Letter, number & special character")

    while True:
        password = input("Enter password: ")
        if is_strong_password(password):
            break
        else:
            print("Weak password")

    with open("users.txt", "a") as file:
        file.write(f"{email}:{hash_password(password)}\n")

    print("Registration successful!")


def login():
    print("\nLogin")

    email = input("Enter email: ").strip().lower()
    password = input("Enter password: ")

    hashed_password = hash_password(password)

    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_email, stored_hash = line.strip().split(":")
                if stored_email == email and stored_hash == hashed_password:
                    print("Login successful!")
                    return
    except FileNotFoundError:
        print("No users registered")

    print("Invalid email or password")


def forgot_password():
    print("\nForgot Password")

    email = input("Enter registered email: ").strip().lower()

    if not email_exists(email):
        print("Email not found")
        return

    print("\nSet a new password")

    while True:
        new_password = input("Enter new password: ")
        if is_strong_password(new_password):
            break
        else:
            print("Weak password")

    new_hash = hash_password(new_password)

    with open("users.txt", "r") as file:
        lines = file.readlines()

    with open("users.txt", "w") as file:
        for line in lines:
            stored_email, _ = line.strip().split(":")
            if stored_email == email:
                file.write(f"{email}:{new_hash}\n")
            else:
                file.write(line)

    print("Password reset successful!")


while True:
    print("\nSecure Login System")
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        forgot_password()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")
