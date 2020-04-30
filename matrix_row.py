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
