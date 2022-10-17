def user_name():
    username = input("please enter username: ")
    return f"welcome {username} "
print(user_name())



password = input("please enter your password")

def length(password):
    if len(password) < 5:
        print("Your Password is Too Short")
    elif len(password) >= 5 and len(password) <= 20:
        print("Your Password is an acceptable length")
    elif len(password) > 20:
        print("your password is too long ")
    else:
        print("error")

length(password)


