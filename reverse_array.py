n= int(input("Enter the no. of elements in an array"))
l=[]
for i in range(0,n):
    a=int(input("Enter the no.of elements"))
    l.append(a)
    print(*l[::-1])    
