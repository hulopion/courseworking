users={}

def register():
    name=input("Enter your name: ")
    email=input("Enter your email address: ")
    password=input("Enter your password: ")
    if(len(password)<=8):
        print("Password shorter than 8 characters, please input a new password")
        password=input("Enter your password: ")
    else:
        print("Valid password")
    
    users[email]= {"name": name, "password": password}
    print("Succesfully registered")
    return users

def login():
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    if email in users:
        if users[email]["password"] == password:
            print(f"Welcome back, {users[email]['name']}!")
        else:
            print("Incorrect password.")
    else:
        print("Email not found. Please register first.")
