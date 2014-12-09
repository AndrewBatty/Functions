





def password_login():
    enter_password = str(input("Please enter your password: "))
    password_length = len(enter_password)
    return (password_length)


def display_password(password_length):
    if password_length < 8:
        print("Password is too short.")
        password_login()
    elif password_length > 16:
        print("Password is too long.")
        password_login()
    else:
        print("Password accepted.")
        password_login()
    return (password_length)



password_length = password_login()
password_login()
