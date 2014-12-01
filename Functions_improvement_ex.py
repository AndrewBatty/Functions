# Andrew Batty
# 01/12/14
# Function Improvement Task 1 - Bank Details

def data_collection():
    first_name = str(input("Please enter your first name: "))
    last_name = str(input("Please enter your last name: "))
    gender = str(input("Please enter your gender: "))
    street_name = str(input("Please enter the name of your street: "))
    town = str(input("Please enter the name of the town you live in: "))
    post_code = str(input("Please enter your post code: "))
    house_number = str(input("Please enter your house number or house name: "))
    return (first_name,last_name,gender,street_name,town,post_code,house_number)


def return_decision(gender):
    if gender == "Male" or "male":
        gender_result = "Mr"
    elif gender == 'Female' or 'female':
        gender_result = "Ms"
    return gender_result


def output_message(gender_result,first_name,last_name):
    output = print("Welcome {0} {1} {2}. Your registation has been successful.".format(gender_result,first_name,last_name))
    return output

def bank_details():
    first_name,last_name,gender,street_name,town,post_code,house_number = data_collection()
    decision = return_decision(gender)
    output_mes = output_message(decision,first_name,last_name)
    return output_mes

bank_details()


