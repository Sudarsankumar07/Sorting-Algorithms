#Bubble sort
#Time complexity O(n^2)
arr = [5,4,3,2,1]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Bubble sort:",arr)

#Selection sort
#Time complexity O(n^2)

for i in range(len(arr)):
    min_idx = i
    for j in range(i+1,len(arr)):
        if arr[j] < arr[min_idx]:
            min_idx = j
    arr[i],arr[min_idx] = arr[min_idx],arr[i]
print("Selection sort:",arr)

#insertion sort
#Time complexity O(n^2)
for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key <=arr[j]:
        arr[j+1] =arr[j]
        j-=1
    arr[j+1] = key
print("Insertion sort:",arr)

#Quick sort
#Time complexityO(n log n)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left)+middle+quick_sort(right)
print("Merge sort:",quick_sort(arr))