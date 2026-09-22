if __name__ == '__main__':
    n = int(input("Enter a number: "))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        print("The factorial of " + str(n) + " is: " + str(result))
