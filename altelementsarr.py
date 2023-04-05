arr=[]
n = int(input("Enter the number of elements you want to enter: "))
for i in range (0,n,1):
    x = int(input(f"Enter the element:{[i+1]}"))
    arr.append(x)
    
print(arr)

for i in range(0,len(arr),2):
    print(arr[i],end=' ')


    