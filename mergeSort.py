def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        merge(left, right, arr)


def merge(arr1, arr2, arr):
    p1 = p2 = p = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            arr[p] = arr1[p1]
            p1 += 1
        else:
            arr[p] = arr2[p2]
            p2 += 1
        p += 1
    while p1 < len(arr1):
        arr[p] = arr1[p1]
        p1 += 1
        p += 1
    while p2 < len(arr2):
        arr[p] = arr2[p2]
        p2 += 1
        p += 1


arrTest = [7, 7, 2, 3, 0, 6, 5, 4, 3, 2, 1, 0]
merge_sort(arrTest)
print(f'Sorted array: {arrTest}')
