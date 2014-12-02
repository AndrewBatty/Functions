# Andrew Batty
# 02/12/14
# Functions class exercises revistion exercises task 1

def input_num_char():
    number = int(input("Please enter a number: "))
    character = str(input("Please enter a character: "))
    return (number,character)

def calculation_return(number,character):
    total = (number * character)
    return total

def display_calc_return(total):
    print(total)

def output_sybols():
    number,character = input_num_char()
    total = calculation_return(number,character)
    display = display_calc_return(total)
    
output_sybols()
