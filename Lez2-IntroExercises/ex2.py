firstNumber = int(input("Enter the first operand: \n"))
secondNumber = int(input("Enter the second operand: \n"))
operator = int(input("Enter the operator: \n - 0 for addition \n - 1 for subtraction \n - 2 for multiplication \n - 3 for division: \n"))


#adding f before the " allows you to insert variables
#inside the string

if operator == 0:
    print(f"solution = {firstNumber + secondNumber}")
elif operator == 1:
    print(f"solution = {firstNumber - secondNumber}")
elif operator == 2:
    print(f"solution = {firstNumber * secondNumber}")
if operator == 3:
    print(f"solution = {firstNumber / secondNumber}")
