import json
import timeit
import matplotlib.pyplot as plt
import threading

# Increase the stack size for threading
threading.stack_size(33554432)

import sys

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

# Read the inputs from the ex2.json file
with open("ex2.json", "r") as f:
    inputs = json.load(f)

# Set the recursion limit to avoid errors for larger inputs
sys.setrecursionlimit(20000)

# Define a list to store the timing results for each input
timing_results = []

# Iterate over each input and time the func1 function
for input_data in inputs:
    arr = input_data
    low = 0
    high = len(arr) - 1
    time = timeit.timeit(lambda: func1(arr, low, high), number=1)
    timing_results.append(time)

# Plot the timing results using matplotlib
plt.plot(timing_results)
plt.title("Timing Results for func1")
plt.xlabel("Input Number")
plt.ylabel("Time (s)")
plt.show()
