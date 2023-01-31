def CountingEvenOdd(arr, arr_size):
	for i in range(arr_size):
		if (arr[i] % 2 == 0):
			evenlist.append(arr)
						
		else:
			oddlist.append(arr)
			


	print(" even elements = ",evenlist)
	print("odd elements = ",oddlist)

evenlist=[]
oddlist=[]

arr =[]
n=int(input("ENter num of elemts:"))
for i in range(n):
	arr.append(int(input("Enter the elements:")))
n = len(arr)
CountingEvenOdd(arr, n)

