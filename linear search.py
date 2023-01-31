def linear_Search(arr, n, key): 
    arr=[]
    
    n=int(input("Enter the number of elements in array:"))
    for i in range (n):
        arr.append(input("Enter the array elemnts:"))
    
    key = int(input("Enter the element to search:"))  

    n = len(arr)  
    a = linear_Search(arr, n, key)  
    if(a == -1):  
        print("Element not found")  
    else:  
        print("Element found at index: ", a)

