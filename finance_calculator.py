#This is a python progaram that lets the user input to select 'bond' or 'investment'.
#if investment was selected it will ask for more info and what kind of investment it is, weather 'simple' or 'compound interest
#The program will do some calculations and print out the return on the investment
#if 'bond' is selected. It asks for info from user regarding the bond then prints out the calculated bond
#if the program does not recognize user input, it prints out the error message 'invalid selection'

import math

print("Select 'bond' or 'investment type' from the list below: \n")

print('bond      \t- to calculate the amount you\'ll have to pay on a home loan')
print('investment\t- to calculate the amount of interest you\'ll earn on interest \n')

selection = input("What would you like to calculate, investment or bond?: ")

if selection == 'investment' or selection == "INVESTMENT" or selection == "Investment":
    deposit = float(input("Please enter the deposit amount: "))
    rate = float(input("Please enter the interest rate: "))
    time = float(input("Please enter the number of year/s: "))
    interest = input("Please enter type of interest, either 'compound' or 'simple' interest: ")

    simple_interest = (deposit * rate * time) / 100
    compound_interest = deposit * (1 + rate / 100)**time

    if interest == 'simple' or interest == 'SIMPLE' or interest == 'Simple':
        print("R" + str(round(simple_interest + deposit)))
    elif interest == 'compound' or interest == 'Compound' or interest == 'COMPOUND':
        print("R" + str(round(compound_interest)))
    else:
        print("Your selection is invalid")


if selection == "bond" or selection == "Bond" or selection == "BOND\n":
    evaluation = int(input("Please enter the value of the house "))
    rate = int(input("Please enter the interest rate: "))
    time = int(input("Please enter the number of months it would take to pay the bond: "))

    interest_rate = rate / 12
    bond = (interest_rate * evaluation)/(1 - (1 + interest_rate)**(-time))
    print("R" + str(round(bond)))

else:
    print("Your selection is invalid!")






