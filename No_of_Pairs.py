#Given two arrays X and Y of positive integers, find the number of pairs such that
#xy > yx (raised to power of) where x is an element from X and y is an element from Y.


def countPairs(X, Y, m, n):
    ans = 0
    for i in range(m):
        for j in range(n):
            if (pow(X[i], Y[j]) > pow(Y[j], X[i])):
                ans += 1
    return ans
    


#driver code
X = [2,3,4,5]
Y = [1,2,3]
m = len(X)
n = len(Y)
print(countPairs(X,Y,m,n))

#Output
#5
