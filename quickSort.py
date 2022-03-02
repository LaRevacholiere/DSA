def swap(arr, start, end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp


def mid_of_three(arr, start, end):
    mid = int(start + (end - start) / 2)
    if (arr[start] < arr[mid] < arr[end]) or (arr[end] < arr[mid] < arr[start]):
        return mid
    if (arr[mid] < arr[start] < arr[end]) or (arr[end] < arr[start] < arr[mid]):
        return start
    else:
        return end


def partition(arr, start, end):
    p = mid_of_three(arr, start, end)
    pivot = arr[p]
    swap(arr, p, end)
    i = j = start
    while j < end:
        if arr[j] < pivot:
            swap(arr, i, j)
            i += 1
        j += 1
    swap(arr, i, end)
    return i


def quick_sort(arr, start, end):
    if start < end:
        p = partition(arr, start, end)
        quick_sort(arr, start, p - 1)
        quick_sort(arr, p + 1, end)


arrTest = [7, 7, 2, 3, 0, 6, 5, 4, 3, 2, 1, 0]
quick_sort(arrTest, 0, len(arrTest) - 1)
print(f'Sorted array: {arrTest}')
