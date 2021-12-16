# Write a python program to find largest of three numbers

number1 = 10
number2 = 20
number3 = 30

if number1 > number2 and number1 > number3:
    print("Largest Number is 1st number : ", number1)
elif number2 > number3 and number2 > number1:
    print("Largest Number is 2nd number : ", number2)
elif number3 > number1 and number3 > number2:
    print("Largest Number is 3rd number : ", number3)
else:
    print("Both Numbers are equal")
