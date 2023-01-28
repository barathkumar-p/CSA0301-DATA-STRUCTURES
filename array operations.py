print("ARRAY")

arr=[]
n=int(input("Enter the number of elements in array:"))
for i in range (n):
    arr.append(input("Enter the array elemnts:"))
#display
print(arr)

print("Choose the operation:")
print("1-INSERT")
print("2-DELETE")
print("3-DISPLAY")
choice=int(input("Enter the choice:"))


if choice==1:
    pos=int(input("ENter the position of array:"))
    ele=int(input("ENter the elemnt:"))
    arr.insert(pos,ele)
    print(arr)
    
elif choice==2:
    pos=int(input("ENter the position of array:"))
    ele=int(input("ENter the elemnt:"))
    arr.remove(pos,ele)
    print(arr)

elif choice==3:
    print(arr)

else:
    print("Invalid choice!")