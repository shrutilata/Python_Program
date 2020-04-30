#Source Code:--

def matrix(a):
    c=1
    r=len(a)
    col=len(a[0])
    for i in range(r):
        if (c%2!=0):
            for j in range (0,col):
                print(a[i][j],end=" ")
            c=c+1
        else:
            for j in range(col-1,-1,-1):
                print(a[i][j],end=" ")
            c=c+1

#Driver Code:--
matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

#Output:--
1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13
