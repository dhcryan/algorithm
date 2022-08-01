# mergesort: divide and conquer , recursive algorithm
def mergesort(array):
    mid = len(array)//2
    if len(array) <= 1:
        return array
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            array[k] = left[i]
            k += 1
            i += 1
        else:
            array[k] = right[j]
            k += 1
            j += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    if j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = mergesort(arr)
for i in arr:
    
    print(i)
