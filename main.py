import sys
import math
from decimal import Decimal

class operations():
    def __init__(self, result):
        self.result = result
    
    def add(num1, num2):
        result = (num1) + (num2)
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
            return (f'The square root of {num1} is {sqrtNum1} {operations.resultInSciNot(sqrtNum1)}. The square root of {num2} is {sqrtNum2} {operations.resultInSciNot(sqrtNum2)}.')

    def cubeRoots(num1, num2):
        cubeRootNum1 = num1**(1/3) 
        cubeRootNum2 = num2**(1/3) 
        return(f"The cube root of {num1} is {cubeRootNum1} {operations.resultInSciNot(cubeRootNum1)}. The cube root of {num2} is {cubeRootNum2} or {operations.resultInSciNot(cubeRootNum2)}.")

    def factorial(num):
        i = num
        for i in range (1, int(num)):
            num = num * i
            i -= 1
        return num

    def log2(num1, num2):
        result1 = math.sqrt(num1)
        result2 = math.sqrt(num2)
        return (f"Log2 {num1} = {result1}. Log2 {num2} = {result2}.")


    def resultInSciNot(result):
        exponent = 0
        isNegative = False
        if result < 0:
            isNegative = True
        result = abs(result)
        if result >= 10:
            while result >= 10:
                result = result * 0.1
                exponent += 1
        elif result < 1:
            while result < 1:
                result = result * 10
                exponent += 1

        result = round(result, 3) # rounding the value to 3 decimal points
        if isNegative == True:
            return(f"or -{result}e{exponent}")
        else:
            return(f"or {result}e{exponent}")

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
                result = operations.add(num1, num2)
                print(f"The addition of {num1} and {num2} yielded {operations.add(num1, num2)}, {operations.resultInSciNot(result)}")
            elif whatToExecute.lower() == "substract" or whatToExecute.lower() == "-":
                result = operations.substract(num1, num2)
                print(f"The substraction of {num1} by {num2} yielded {operations.substract(num1, num2)}, {operations.resultInSciNot(result)}")
            elif whatToExecute.lower() == "multiply" or whatToExecute.lower() == "*":
                result = operations.multiply(num1, num2)
                print(f"The multiplication of {num1} by {num2} yielded {operations.multiply(num1, num2)}, {operations.resultInSciNot(result)}")
            elif whatToExecute.lower() == "divide" or whatToExecute.lower() == "/":
                if num2 == 0:
                    print("Division by zero is not possible!")
                else: 
                    result = operations.divide(num1, num2)
                    print(f"The division of {num1} by {num2} yielded {operations.divide(num1, num2)}, {operations.resultInSciNot(result)}")
            elif whatToExecute.lower() == "sqrt" or whatToExecute.lower() == "square root":
                print(operations.squareRoots(num1, num2))     
            elif whatToExecute.lower() == "cbroot" or whatToExecute.lower() == "cube root":
                print(operations.cubeRoots(num1, num2))
            elif whatToExecute.lower() == "fact" or whatToExecute.lower() == "factorial":
                print(operations.factorial(num1), operations.factorial(num2))
            elif whatToExecute.lower() == "log2":
                print(operations.log2(num1, num2))
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
