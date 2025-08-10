def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i

        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        
        arr[j] = key
        
def SelectionSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
            

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  
    i = low - 1 

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return i + 1



ll = [8, 6, 9, 0, 7, 4, 3, 1, 2, 5]

quicksort(ll, 0, len(ll) - 1)

print(ll)