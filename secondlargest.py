# arr = [1,9,3,3,5,5,6,7]
# arr = list(set(arr))
# print(arr)
length = int(input("Enter len: "))
# arr=[None]*length
arr=[]

#n=int(input("Enter the number of elements: "))


for i in range(0,length,1):
    x = int(input(f"Enter the element{i+1}: "))
#     arr[i]=x
    
    
    arr.append(x)
    
    
print(arr)
arr.sort()
print(arr)
arr[length-2]=str(arr[length-2])
print(f"The second largest number is: {arr[length-2]}")

    