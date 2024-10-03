from .Registration import dict_
def login():
    username=input("Enter the username")
    password=input("Enter the password")
    if dict_["username"]==username and dict_["passw"]==password:
        print("LOGIN SUCCESSFUL")
        return True
    else:
        print(f"INVALID {username} or {password}")
        return False    

