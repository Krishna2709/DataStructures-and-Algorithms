# Merge Sort
# TimeComplexity - O(nlogn)

def Merge(a,b):
    mergedArray = []
    while len(a) != 0 and len(b) != 0 :
        if a[0] < b[0]:
            mergedArray.append(a[0])
            a.remove(a[0])
        else:
            mergedArray.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        mergedArray += b
    else:
        mergedArray += a
    return mergedArray

def MergeSort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        mid = int(len(arr)/2)
        a = MergeSort(arr[:mid])
        b = MergeSort(arr[mid:])
        return Merge(a,b)

'''
arr = [44,34,52,12,22,84,90,20,32]
print(MergeSort(arr))
'''