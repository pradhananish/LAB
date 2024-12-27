from random import sample
from time import time
from quick import quick_sort
from merge import merge_sort
import matplotlib.pyplot as plt

def runQuickSort(n):
    data = sample(range(n+1), n)
    start_time = time() * 1000
    quick_sort(data, 0, len(data) - 1)
    end_time = time() * 1000
    return end_time - start_time

def runMergeSort(n):
    data = sample(range(n+1), n)
    start_time = time() * 1000
    merge_sort(data, 0, len(data) - 1)
    end_time = time() * 1000
    return end_time - start_time

if __name__ == "__main__":
    inpSize = []
    execTimeQuickSort = []
    execTimeMergeSort = []

    for i in range(0, 25001, 5000):
        inpSize.append(i)
        execTimeQuickSort.append(runQuickSort(i))
        execTimeMergeSort.append(runMergeSort(i))

    plt.xlabel("Input Size")
    plt.ylabel("Time (ms)")
    plt.plot(inpSize, execTimeQuickSort, label="Quick Sort")
    plt.plot(inpSize, execTimeMergeSort, label="Merge Sort")
    plt.legend()
    plt.title("Quick Sort vs Merge Sort Performance")
    plt.show()
