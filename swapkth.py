arr = [1,2,3,4,5,6]
k = int(input('Enter the postion you want to swap: '))
temp = arr[k-1]
arr[k-1] = arr[len(arr)-k]
arr[len(arr)-k]=temp

print(arr)
      