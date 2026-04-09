# Function to find greatest of three numbers
def greatest(a, b, c):
    if a >= b and a >= c:
        print("Greatest number is:", a)
    elif b >= a and b >= c:
        print("Greatest number is:", b)
    else:
        print("Greatest number is:", c)

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Calling the function
greatest(num1, num2, num3)
