# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

def heapif(arr, n, i):
    large = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[large]:
        large = left

    if right < n and arr[right] > arr[large]:
        large = right

    if large != i:
        arr[i], arr[large] = arr[large], arr[i]
        heapif(arr, n, large)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapif(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapif(arr, i, 0)

arr = [11, 14, 13, 5, 6, 7]
heap_sort(arr)
print("Отсортированный массив:")
print(arr)
