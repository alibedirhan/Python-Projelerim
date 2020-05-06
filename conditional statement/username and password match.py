sys_user_name= "abc"
sys_user_password = "123456"

access_right = 3

while True:
    user_name = input("User Name :")
    password = input("Password :")
    if (user_name != sys_user_name and password == sys_password):
        print("Enter a valid user name")
        access_right -=1
        print("Access Right :", access_right )
    elif (user_name == sys_user_name and password != sys_password):
        print("Password wrong")
        access_right -=1
        print("Access Right :", access_right)
    elif (user_name != sys_user_name and password !=sys_password):
        print("Enter a valid user name and password")
        access_right -=1
        print("Access Right :", access_right)
    else:
        print("Login to the system")
        break
    if (access_right == 0):
        print("You have no access right")
        break
