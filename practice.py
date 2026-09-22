##Hello world
'''
print("hello world")
'''
## wap to check user is eligible for vote or not??

'''
age = int(input("Enter Your Age: "))
if age >=18: 
    print("You are Eligible for Vote")
else:
    print("You are not Eligible for Vote")
'''

## wap to check no. is +ve or -ve??
'''
num1 = int(input("Enter a Number: "))
if num1 > 0: 
    print("The Number is Positive")
elif num1 < 0: 
    print("The number is Negative")
else:
    print("The Number is Zero")
'''

## wap to check no. is even or not??
'''
num1 = int(input("Enter a Number: "))
if num1 % 2 == 0: 
    print('The number is Even')
else:
    print("The number is Odd")
'''
## Compare a no with 17 if no. is gretre than 17 then return absolute diff if not return square of diff??

num1 = int(input("Enter a Number: "))
if num1 > 17:
    print(f"The Number is Greater than 17, The absolute difference between 17 and Num1 is: {num1-17}")
elif num1 < 17:
    diff = 17 - num1
    square = diff ** 2
    print(f"The number is Lesser than 17 so the Square of the Diffrence of 17 and Num1 is: {square}")
else: 
    print("Num1 is equal to 17")