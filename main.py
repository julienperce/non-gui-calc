import sys
import math

class operations():
    def __init__(self, result):
        self.result = result
    
    def add(num1, num2):
        result = num1 + num2
        return result

    def substract(num1, num2):
        result = num1 - num2
        return result

    def multiply(num1, num2):
        result = num1 * num2
        return result

    def divide(num1, num2):
        result = num1 / num2
        return result

def mainCalc():
    if __name__ == "__main__":
        correctValues = False
        while correctValues == False:
            try:
                num1 = float(input("Select your first number: "))
                num2 = float(input("Select your second number: "))
                correctValues = True
            except ValueError:
                print("It looks like one of the values you entered was not a number! Please try again.")
                correctValues = False
        if correctValues == True:
            whatToExecute = str(input("What mathematical operation would you like to solve? "))
            if whatToExecute.lower() == "add" or whatToExecute.lower() == "+": 
                print(f"The addition of {num1} and {num2} yielded {operations.add(num1, num2)}")
            elif whatToExecute.lower() == "substract" or whatToExecute.lower() == "-":
                print(f"The substraction of {num1} by {num2} yielded {operations.substract(num1, num2)}")
            elif whatToExecute.lower() == "multiply" or whatToExecute.lower() == "*":
                print(f"The multiplication of {num1} by {num2} yielded {operations.multiply(num1, num2)}")
            elif whatToExecute.lower() == "divide" or whatToExecute.lower() == "/":
                if num2 == 0:
                    print("Division by zero is not possible!")
                else: 
                    print(f"The division of {num1} by {num2} yielded {operations.divide(num1, num2)}")      
            else:
                print("It looks like you are attempting an operation that is not supported!")

wantToExecute = True
userWantsToExecute = str(input("Would you like to solve a mathematical operation today? "))
if userWantsToExecute.lower() == "n" or userWantsToExecute.lower() == "no":
    sys.exit(0)

while wantToExecute == True:
    mainCalc()
    wantsToExecuteAnother = str(input("Would you like to solve another operation?"))
    if wantsToExecuteAnother.lower() == "n" or wantsToExecuteAnother.lower() == "no":
        wantToExecute = False
