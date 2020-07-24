num1 = int(input("Enter number"))
num2 = int(input("Enter number"))
num3 = int(input("Enter number"))
for x in range(1, num3+1):
    if x % num1 == 0 and x % num2 == 0:
        print("FizzBuzz", end=' ')
    elif x % num1 == 0:
        print("Fizz", end=' ')
    elif x % num2 == 0:
        print("Buzz")
    else:
        print(x, end=' ')

