#!/usr/bin/python

# Prime Number
def primenumCheck(option):	

    if option > 1:
        for i in range(2,option):
            if (option % i) == 0:
                print(option,"is not a prime number")
                print(i,"times",option//i,"is",option)
                break
        else:
            print(option,"is a prime number")

    else:
        print(option,"is not a prime number")

# Armstrong Number
def ArmstrongCheck(option):

    sum = 0

    temp = option

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //=10

    if option == sum:
        print(option,"is an Armstrong Number")
    else:
        print(option,"is not an Armstrong Number")

def Factorial(option):

    result = 1

    if option == 0:
        print("Factorial of 0 is 1")

    elif option < 0:
        print("Cannot Calculate Factorial for a Negative Number")

    else:
        for i in range(1,option + 1):
            result = result * i
        print("The factorial of",option,"is",result)


option = int(input("Enter a number to Check if it is a Prime Number,Armstrong Number and Find Factorial:"))

primenumCheck(option)
ArmstrongCheck(option)
Factorial(option)
