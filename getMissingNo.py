#Missing number in array 
#Complete the function MissingNumber() that takes array and N as input and returns the value of the missing number.


#def getMissingNo(A):
  #  n=len(A)
    #total = (n+1)*(n+2)/2
    #sum_of_A = sum(A)
    #return total - sum_of_A

#A = [1, 2, 4, 5, 6]
#miss = getMissingNo(A)
#print(miss)

  #OR

def MissingNumber(a,n):
    total = (n*(n+1)/2)
    sum=0
    for i in range (len(a)):
        sum += a[i]
        s = total-sum

    print(s)

#driver code
a=[1,2,4,5,6]
s = MissingNumber(a,6)

