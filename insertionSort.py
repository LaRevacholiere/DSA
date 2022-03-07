def insertion_sort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


arrTest = [7, 7, 2, 3, 0, 6, 5, 4, 3, 2, 1, 0]
insertion_sort(arrTest)
print(f'Sorted array: {arrTest}')
