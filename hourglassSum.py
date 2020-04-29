#Source Code:--

def hourglassSum(arr):
    max_sum=0
    for i in range(0,6):
        for j in range(0,6):
                if(i+2 < 6 and j+2 < 6):
                    sum=a[i][j]+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
                    #print(a(i,j))
                    #print(a(i,j+1))
                    #print(a(i,j+2))
                    #print(a(i+1,j+1))
                    
                    #+a[i][j+1]+a[i][j+2]+a[i+1][j+1]+a[i+2][j]+a[i+2][j+1]+a[i+2][j+2]
                    if(sum>max_sum):
                        max_sum = sum
    return max_sum

#Driver Code:--
hourglassSum([[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0,],[0,0,2,4,4,0],[0, 0, 0, 2, 0, 0],[0, 0, 1, 2, 4, 0]])

#Output:--
19
