# *****Write the Program to Handle User Input
# name = input("Please enter your name: ")
# last_name = input("Please enter your last name: ")

# if name and last_name:
#     print("Welcome", name, last_name)
# else:
#     print("Error: You must enter your name and last name.")
user_name= "admin"
password= "password123"
N=input("please enter your user name : ")
P=input("please enter your password: ")
if user_name == N and password == P :
    print("login successful")
elif user_name != N and password == P:
    print("ERROR invalid user name ")
elif user_name ==N and password != P :
    print(" ERROR invalid password ")
else:
    print("ERROR both user name and password are incorrect")

