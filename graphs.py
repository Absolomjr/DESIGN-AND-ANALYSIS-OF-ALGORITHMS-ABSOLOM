#Implementing and Analyzing Sorting Algorithms
#1. Importing Necessary Libraries:
import time
import matplotlib.pyplot as plt
import numpy as np

#2. Implementing Sorting Algorithms:
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

#3. Timing the Algorithms and Plotting:
def time_sort(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return (end_time - start_time) * 1000  # Convert to milliseconds

def plot_time_complexity(sort_funcs, input_sizes):
    time_data = []
    for sort_func in sort_funcs:
        func_times = []
        for n in input_sizes:
            arr = np.random.randint(1, 1000, n)
            time_taken = time_sort(sort_func, arr.copy())
            func_times.append(time_taken)
        time_data.append(func_times)

    plt.plot(input_sizes, time_data[0], label="Bubble Sort")
    plt.plot(input_sizes, time_data[1], label="Insertion Sort")
    plt.plot(input_sizes, time_data[2], label="Selection Sort")
    plt.plot(input_sizes, time_data[3], label="Merge Sort")
    plt.plot(input_sizes, time_data[4], label="Quick Sort")
    plt.plot(input_sizes, time_data[5], label="Heap Sort")

    plt.xlabel("Input Size")
    plt.ylabel("Time (ms)")
    plt.title("Time Complexity of Sorting Algorithms")
    plt.legend()
    plt.grid(True)
    plt.show()

#4. Running the Code:
if __name__ == "__main__":
    sort_funcs = [bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort, heap_sort]
    input_sizes = [10, 100, 500, 1000, 2000, 5000]
    plot_time_complexity(sort_funcs, input_sizes)

# Explanation:
#  * Implementations: We implement the standard sorting algorithms.
#  * Timing Function: The time_sort function measures the execution time of each algorithm.
#  * Plotting Function: The plot_time_complexity function:
#    * Generates random arrays of different sizes.
#    * Times each algorithm
