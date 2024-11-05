import random
import matplotlib.pyplot as plt
import time

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def time_sorting(sorting_algorithm, data):
    start_time = time.time()
    sorting_algorithm(data)
    return time.time() - start_time

def measure_time(n):
    arr = random.sample(range(n), n)  # Random array of size n
    quick_time = time_sorting(quick_sort, arr.copy())
    insertion_time = time_sorting(insertion_sort, arr.copy())
    merge_time = time_sorting(merge_sort, arr.copy())
    return quick_time, insertion_time, merge_time




def plot_sorting_times(sizes):
    quick_times = []
    insertion_times = []
    merge_times = []

    for size in sizes:
        qt, it, mt = measure_time(size)
        quick_times.append(qt)
        insertion_times.append(it)
        merge_times.append(mt)

    plt.figure(figsize=(12, 6))
    plt.plot(sizes, quick_times, label='Quick Sort', marker='o')
    plt.plot(sizes, insertion_times, label='Insertion Sort', marker='o')
    plt.plot(sizes, merge_times, label='Merge Sort', marker='o')
    
    plt.title('Sorting Algorithm Time Complexity Comparison')
    plt.xlabel('Size of Array')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid()
    plt.show()

# Define sizes of arrays to test
sizes = [100, 200, 400, 800, 1600, 3200, 6400]
plot_sorting_times(sizes)

measure_time(300)