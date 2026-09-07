
import time

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]

coins = list(map(int, input("Enter coin denominations separated by spaces: ").split()))
amount = int(input("Enter the amount: "))

start_time = time.perf_counter()

result = min_coins(coins, amount)

end_time = time.perf_counter()

execution_time = end_time - start_time

if result == float('inf'):
    print("\nChange cannot be made for the given amount.")
else:
    print("\nMinimum number of coins required:", result)

print("Execution Time:", execution_time, "seconds")

print("\nTime Complexity: O(n × amount)")
print("Space Complexity: O(amount)")
