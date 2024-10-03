dict_={}
# def register(username,password):
def register():
    username=input("enter the name")
    password=input("enter the pass")
    c_password=input("Enter the confirm pass")
    if password==c_password:
        print("Registration Successful")
    else:
        print("Password mis matching")
    dict_["username"]=username
    dict_["passw"]=password
 
    return dict_
     

