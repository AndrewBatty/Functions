# Andrew Batty
# 18/11/14
# Functions Stater Part 1 task 4

#difining basic pay
def calculate_basic_pay(hours,pay):
    basic_pay = hours * pay
    return basic_pay

#defining overtime pay
def calculate_overtime_pay(hours,pay):
    over_hours = hours - 40
    over_pay = pay * 1.5
    overtime_pay = over_hours * over_pay
    basic_pay = 40 * pay
    total_pay = basic_pay + overtime_pay
    return total_pay

def calculate_total_pay(hours,pay):
    if hours <= 40:
        total_pay = calculate_basic_pay(hours,pay)
    else:
        total_pay = calculate_overtime_pay(hours,pay)
    return total_pay

def work_details():
    hours = int(input("Please enter the amount of hours you have worked this week: "))
    pay = float(input("Please enter your normal rate of pay: "))
    return (hours,pay)

def diplay_total_pay(total_pay):
    print
    

#main program

    
