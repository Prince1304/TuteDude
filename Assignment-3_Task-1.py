def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number: "))
answer = int(factorial(n))
print(f"The Factorial Of {n} is {answer}")