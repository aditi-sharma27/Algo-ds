# fibo series [0,1,1,2,3,5,8,13,21]


# Function for nth Fibonacci number
def fibonacci(n):
    if n < 0:
        return "Invalid input"
    elif n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(8))
