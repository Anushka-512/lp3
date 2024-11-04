# Function to calculate Fibonacci series non-recursively
def fibonacci_non_recursive(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
# Function to calculate the nth Fibonacci number recursively
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# Function to display Fibonacci series using recursion
def display_fibonacci_recursive(n):
    fib_series = [fibonacci_recursive(i) for i in range(n)]
    return fib_series
# Main program loop
while True:
    try:
        n = int(input("Enter the number of terms for Fibonacci series: "))
        if n < 0:
            print("Please enter a positive integer.")
            continue
        
        # Non-recursive Fibonacci series
        print("Fibonacci series (Non-Recursive):", fibonacci_non_recursive(n))
        
        # Recursive Fibonacci series
        print("Fibonacci series (Recursive):", display_fibonacci_recursive(n))
        
    except ValueError:
        print("Invalid input. Please enter an integer.")

    # Check if the user wants to continue or exit
    choice = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Exiting program.")
        break


