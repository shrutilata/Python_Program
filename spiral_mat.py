#Source Code:-

def spiral_mat(mat):

    top=left=0
    bottom=len(mat)
    right=len(mat[0])
    l=[]

    while(True):
        if(left>right):
            break

        for i in range(left,right):
            #print (mat[top][i],end=" ")
            l.append(mat[top][i])
        top=top+1

        if(top>bottom):
            break

        for i in range(top,bottom):
            #print (mat[i][right-1],end=" ")
            l.append(mat[i][right-1])
        right=right-1

        if(left>right):
            break


        for i in range(right,left,-1):
            #print(mat[bottom-1][i-1],end=" ")
            l.append(mat[bottom-1][i-1])
        bottom=bottom-1

        if(top>bottom):
            break

        for i in range(bottom,top,-1):
            #print(mat[i-1][left],end=" ")
            l.append(mat[i-1][left])
        left=left+1
        
    return l

#Driver Code:-

spiral_mat([[1,2,3,4],
        [12,13,14,5],
        [11,16,15,6],
        [10,9,8,7]])

#output:-

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

