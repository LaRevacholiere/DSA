def selection_sort(arr):
    for i in range(len(arr)):
        min_num = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_num]:
                min_num = j
        swap(arr, min_num, i)


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


arrTest = [7, 7, 2, 3, 0, 6, 5, 4, 3, 2, 1, 0]
selection_sort(arrTest)
print(f'Sorted array: {arrTest}')
