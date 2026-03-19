def login(user, password):
    correct_password = "12345"   # moved to variable (still simple, but better practice)
    
    if password == correct_password:
        print("Login successful")
    else:
        print("Login failed")

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero")
        return None
    return a / b

login("admin", "12345")
result = divide(10, 0)

if result is not None:
    print(result)