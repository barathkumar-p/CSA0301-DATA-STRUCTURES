'''def linear_Search(list1, n, key):  

    list1 = [1 ,3, 5, 4, 7, 9]  
    key = 7  
    
    n = len(list1)  
    res = linear_Search(list1, n, key)  
    if(res == -1):  
        print("Element not found")  
    else:  
        print("Element found at index: ", res) '''

# Linear Search in Python


def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = int(input("enter element:"))
n = len(array)
result = linearSearch(array, n, x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)