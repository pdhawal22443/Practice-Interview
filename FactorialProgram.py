def factorial(num):
    if num ==1:
        return 1
    else:
        return num * factorial(num - 1)


print("Factorial of 5 is {}".format(factorial(5)))


