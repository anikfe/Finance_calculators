# finance calculator for investement and home loan repaymentinvestemnt
import math

calculation_types = input("""investment - to calculate the amount of interest you'll earn on your investement
bond       - to calculate the amount you'll have to pay on a home loan\n
Enter either 'investnent' or 'bond' from the menu above to proceed: """) 

# FOR INVESTMENT
# formula for simple interst: A = P*(1 + r*t)
# compound interest: A = P* math.pow((1+r),t)
# r is the interest divided by 100
# P is amount that user deposits
# t is number of years money is being invested
# A is total amount once interest has been applied

# # FOR BOND
# repayment formula: repayment = (i * P)/(1 + i)**(-n))
# P is present house value
# i is monthly interest rate, calculated by dividing the annual interest rate by 12 (and then divide by 100):
# n is number of months over whuch the bond will be repaid
# these values can't be strings, i want them as floats, because mortgage rates are never whole numbers

if (calculation_types.lower() == "investment"): # "How the user capitalises their selection should not affect how the program proceeds" hence .lower funcion
    # r:
    interest_rate = float(input("What is the interest rate? Please enter only the number: "))/100 # ref for float function I used: https://www.w3schools.com/python/ref_func_float.asp
    # P:
    deposited_amount = float(input("Please enter the amount you want to deposit: "))
    # t: 
    time_length =int(input("For how many years do you want to invest? "))
    # define which type of interest:
    interest = input("Do you want 'simple' or 'compound' interest? ")

    if (interest.lower() == "simple"):
        A = deposited_amount*(1 + interest_rate*time_length)
        print(f"Your investment will be worth: {round(A, 2)} after {time_length} years") # used round function to round to 2 decimal points ref: https://www.w3schools.com/python/ref_func_round.asp
    elif (interest.lower() == "compound"):
        A = deposited_amount* math.pow(1+interest_rate,time_length)
        print(f"Your investment will be worth: {round(A, 2)} after {time_length} years.") 
    else:
        print("Wrong command")

elif (calculation_types.lower() == "bond"):
    # P:
    house_value = float(input("Please enter the house value: "))
    # i:
    bond_interest = (float(input("Please enter the interest rate: "))/12)/100
    # n:
    months_number = int(input("Please enter how many months you want the bond to be repaid in: "))

    repayment = (bond_interest * house_value)/(1 - (1 + bond_interest)**(-months_number))
    print(f"Your monthly payments will be: {round(repayment, 2)} for {months_number} months.")

else:
    print("Error. Wrong command")
    


# !!! during classes we were told that it is best to define all variables at the top!!!
# !!! that is what I tried to do initially and my code looked like this: !!!
'''
import math

calculation_types = input("""investment - to calculate the amount of interest you'll earn on your investement
bond       - to calculate the amount you'll have to pay on a home loan\n
Enter either 'investnent' or 'bond' from the menu above to proceed: """)
# FOR INVESTMENT
# formula for simple interst: A = P(1 + rxt) for python: A = P*(1 + r*t)
# compound interest: A = P(1 + r)**t for python: A = P* math.pow((1+r),t)
# r is the interest divided by 100
# P is amount that user deposits
# t is number of years money is being invested
# A is total amount once interest has been applied
# simple_interest = P*(1 + r*t)
# r:
interest_rate = int(input("What is the interest rate? Please enter only the number: "))/100
# P:
deposited_amount = int(input("Please enter the amount you want to deposit: "))
# t:
time_length = int(input("For how many years do you want to invest? "))
# after that ask if user wants simple or compound interest
interest = input("Do you want 'simple' or 'compound' interest? ")

# FOR BOND
# repayment formula: repayment = (i * P)/(1 + i)**(-n))
# present house value = 'P':
house_value = int(input("Please enter the house value: "))
# monthly interest rate, calculated by dividing the annual interest rate by 12 - 'i':
bond_interest = (int(input("Please enter the interest rate: "))/12)/100
# number of months over whuch the bond will be repaid - 'n':
months_number = int(input("Please enter how many moths you want the bond to be repaid in: "))
# the formula:
repayment = (bond_interest * house_value)/(1 - (1 + bond_interest)**(-months_number))


if (calculation_types.lower() == "investment"):
    print(interest_rate)
    print(deposited_amount)
    print(time_length)
    print(interest)
    if (interest.lower() == "simple"):
        A = deposited_amount*(1 + interest_rate*time_length)
        print(A)
    elif (interest.lower() == "compound"):
        A = deposited_amount* math.pow(1+interest_rate,time_length)
        print(A)
    else:
        print("Wrong command")
elif (calculation_types.lower() == "bond"):
    print(house_value)
    print(bond_interest)
    print(months_number)
    print(repayment)
else:
    print("Error. Wrong command")'''

# !!! However this did not want to run properly, it was going through each line of code one by one
# no matter what I entered
# when I entered 'bond' it would still ask me for interest instead of house value
# when enterted enything, for example: abcd, instead of displaying error, again it would ask me for interest rate
# this is example of one of the run tests:

# investment - to calculate the amount of interest you'll earn on your investement
# bond       - to calculate the amount you'll have to pay on a home loan

# Enter either 'investnent' or 'bond' from the menu above to proceed: bond
# What is the interest rate? Please enter only the number: 5
# Please enter the amount you want to deposit: 20000
# For how many years do you want to invest? 10
# Do you want 'simple' or 'compound' interest? simple
# Please enter the house value: 250000
# Please enter the interest rate: 20
# Please enter how many moths ypu want the bond to be repaid in: 240
# 250000
# 0.016666666666666666
# 240
# 4247.061518899304

# I didn't know what to do, so I asked in chat GPT and it suggested to put my variables in the if statements
# I tried and it is now working