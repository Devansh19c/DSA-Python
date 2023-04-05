arr=[]
temp=0
n=int(input("Enter the number of elements you want: "))
for i in range(0,n,1):
    x = int(input(f"Enter the number:{[i+1]}"))
    arr.append(x)
    
print(arr)
for i in arr:
    temp +=i

print(temp)

#METHOD 2
# for i in range(len(arr)):
#     temp +=arr[i]

# print(temp)
