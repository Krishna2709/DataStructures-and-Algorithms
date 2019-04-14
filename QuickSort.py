# QuickSort 
# TimeComplexity - O(n^2)

def partition(arr, start, end):
    pivot = follower = start
    while pivot < end:
        if arr[pivot] <= arr[end]:
           arr[follower], arr[pivot] = arr[pivot], arr[follower]
           follower += 1
        pivot += 1
    arr[follower], arr[end] = arr[end], arr[follower]
    return follower

def QuickSort(arr, start, end):
    if start < end:
        p = partition(arr,start,end)
        QuickSort(arr,start, p-1)
        QuickSort(arr,p+1,end)
    return arr

'''
arr = [44,34,52,12,22,84,90,20,32]
print(QuickSort(arr, 0, len(arr)-1))
'''