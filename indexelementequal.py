arr=[]
a=[]
n = int(input("Enter the number of elements: "))
for i in range(0,n,1):
    x=int(input(f"Enter the number:{[i+1]}"))
    arr.append(x)
    
for i in range(len(arr)):
    if(arr[i]==i+1):
        a.append(i+1)
        
print(a)