# Write a python program to find factorial of a number using recursion

def findFactorial(num):
    if num == 1:
        return 1
    return num * findFactorial(num - 1)


number1 = 5
factorial = findFactorial(number1)
print(factorial)
