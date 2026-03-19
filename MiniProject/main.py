def login(user, password):
    if password == "12345":   
        print("Login successful")
    else:
        print("Login failed")

def divide(a, b):
    return a / b   

login("admin", "12345")
print(divide(10, 0)) 