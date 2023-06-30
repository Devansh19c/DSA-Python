# x =bin(int(input("Enter the number: ")))[2::]
x =bin(int(65))[2::]
x = list(x) 
# x = x.split()  ALTERNATE APPROACH TO CREATING A LIST

# print(type(x))
for i in range(len(x)):
    
    if (i==len(x)-1):
        x[i] = str(int(x[i]) ^ 1)
# print(x)
# print(type(x[1]))
y = "".join((x))
print(type(y))
print(chr(int(y,2))) 