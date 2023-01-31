
def search(arr,n):
    a=0
    for i in range(len(arr)):
        if arr[i]==n:
            return "Found",a
        a+=1
    return "Not found"

arr=[]
'''n=int(input("ENter the number of elements:"))
for j in range(n):
    arr.append(int(input("Enter the elements:")))'''

n=int(input("enter the search elemnt:"))

if search(arr,n):
    print("Element found at pos",pos+1)
else:
    print("Element not found")