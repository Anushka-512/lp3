def knapsack_dp(capacity, weights, values, n):
    # Initialize a table to store the maximum value for each subproblem
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    # Build the table dp[][] in a bottom-up manner
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # The last cell of the table contains the maximum value for the knapsack capacity
    return dp[n][capacity]

# Main program loop
while True:
    try:
        # Get knapsack capacity and item details from the user
        capacity = int(input("Enter the capacity of the knapsack: "))
        n = int(input("Enter the number of items: "))

        weights = []
        values = []

        print("Enter the weight and value for each item:")
        for i in range(n):
            weight = int(input(f"Weight of item {i + 1}: "))
            value = int(input(f"Value of item {i + 1}: "))
            weights.append(weight)
            values.append(value)

        # Solve the 0-1 Knapsack problem using dynamic programming
        max_value = knapsack_dp(capacity, weights, values, n)
        print(f"The maximum value that can be carried in the knapsack is: {max_value}")

    except ValueError:
        print("Invalid input. Please enter integers for capacity, weights, and values.")

    # Check if the user wants to continue or exit
    choice = input("Do you want to solve another knapsack problem? (yes/no): ").strip().lower()
    if choice != 'yes':
        print("Exiting program.")
        break
