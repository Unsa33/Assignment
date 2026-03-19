import hashlib
import os


def login(user, password):
    

    stored_password_hash = os.environ.get("APP_PASSWORD_HASH")

    if not stored_password_hash:
        raise EnvironmentError("APP_PASSWORD_HASH environment variable is not set.")

    
    input_hash = hashlib.sha256(password.encode()).hexdigest()

    if input_hash == stored_password_hash:
        print("Login successful")
        return True
    else:
        print("Login failed")
        return False


def divide(a, b):
    """
    Safely divide two numbers, raising a clear error on division by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b



if __name__ == "__main__":


    try:
        login("admin", os.environ.get("APP_PASSWORD", ""))
    except EnvironmentError as e:
        print(f"Configuration error: {e}")

    try:
        print(divide(10, 0))
    except ValueError as e:
        print(f"Math error: {e}")