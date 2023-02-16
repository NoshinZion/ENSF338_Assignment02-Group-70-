import json
import timeit
import matplotlib.pyplot as plt
import threading
import queue

# Increase the stack size for threading
threading.stack_size(33554432)

import sys

def func1(arr, low, high, q):
    if low < high:
        pi = func2(arr, low, high)
        q.put((low, pi-1))
        q.put((pi+1, high))
        func1(arr, low, pi-1, q)
        func1(arr, pi+1, high, q)

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

def worker(arr, q):
    while not q.empty():
        low, high = q.get()
        func1(arr, low, high, q)

# Read the inputs from the ex2.json file
with open("ex2.json", "r") as f:
    inputs = json.load(f)

# Set the recursion limit to avoid errors for larger inputs
sys.setrecursionlimit(20000)

# Define a list to store the timing results for each input
timing_results = []

# Define the number of threads to use
num_threads = 8

# Iterate over each input and time the func1 function
for input_data in inputs:
    arr = input_data
    low = 0
    high = len(arr) - 1

    # Create a queue to store the subarrays to sort
    q = queue.Queue()
    q.put((low, high))

    # Create a list to store the threads
    threads = []

    # Create and start the threads
    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(arr, q))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Add the timing result to the list
    time = timeit.timeit(lambda: func1(arr, low, high, q), number=1)

    timing_results.append(time)

# Plot the timing results using matplotlib
plt.plot(timing_results)
plt.title("Timing Results for func1")
plt.xlabel("Input Number")
plt.ylabel("Time (s)")
plt.show()
