def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0 or n == 1:
        return n
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        memo[n] = result
        return result

