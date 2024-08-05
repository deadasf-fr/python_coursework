def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

def main():
    try:
        n = int(input("Enter the value of n to compute the nth Fibonacci number: "))
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
