import time
import matplotlib.pyplot as plt

# Original Fibonacci implementation
def fibonacci_original(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_original(n-1) + fibonacci_original(n-2)

# Memoized Fibonacci implementation
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = result
        return result

# Time both implementations for inputs 0-35
n_values = list(range(100))
original_times = []
memo_times = []
for n in n_values:
    start_time = time.time()
    fibonacci_original(n)
    original_time = time.time() - start_time
    original_times.append(original_time)
    
    start_time = time.time()
    fibonacci_memo(n)
    memo_time = time.time() - start_time
    memo_times.append(memo_time)

# Plot the results
plt.plot(n_values, original_times, label='Original')
plt.plot(n_values, memo_times, label='Memoized')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.title('Fibonacci Computation Time')
plt.legend()
plt.show()