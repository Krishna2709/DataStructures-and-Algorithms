# Bubble Sort 

def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

'''
arr = [44,34,52,12,22,84,90,20,32]
print(BubbleSort(arr)) 
'''