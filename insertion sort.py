def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
                
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            
        # Place key at after the element just smaller than it.
        arr[j + 1] = key

arr=[]
n=int(input("Enter the number of elements in array:"))
for i in range (n):
    arr.append(input("Enter the array elemnts:"))
    
print("Unsorted Array:", arr)

a=sorted(arr)
print('Sorted Array: ', a)