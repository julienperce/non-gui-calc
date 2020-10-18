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
    
    def squareRoots(num1, num2):
        if num1 < 0 or num2 < 0:
            sqrtNum1 = math.sqrt(abs(num1))
            sqrtNum2 = math.sqrt(abs(num2))
            if num1 < 0:
                return (f'The square root of {num1} is {sqrtNum1}i. The square root of {num2} is {sqrtNum2}.')
            elif num2 < 0:
                return (f'The square root of {num1} is {sqrtNum1}. The square root of {num2} is {sqrtNum2}i.')
            elif num1 < 0 and num2 < 0:
                return (f'The square root of {num1} is {sqrtNum1}i. The square root of {num2} is {sqrtNum2}i.')
        else:
            sqrtNum1 = math.sqrt(num1)
            sqrtNum2 = math.sqrt(num2)
            return (f'The square root of {num1} is {sqrtNum1}. The square root of {num2} is {sqrtNum2}')

    def cubeRoots(num1, num2):
        cubeRootNum1 = num1**(1/3) 
        cubeRootNum2 = num2**(1/3) 
        return(f"The cube root of {num1} is {cubeRootNum1}. The cube root of {num2} is {cubeRootNum2}.")
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
            elif whatToExecute.lower() == "sqrt" or whatToExecute.lower() == "square root":
                print(operations.squareRoots(num1, num2))     
            elif whatToExecute.lower() == "cbroot" or whatToExecute.lower() == "cube root":
                print(operations.cubeRoots(num1, num2))
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
