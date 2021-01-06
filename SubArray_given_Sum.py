Question:-- Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Solution:--

def find_subarray_sum(n,sum):
    curr_sum = 0
    for i in range(len(n)):
        curr_sum = n[i]
        #print (n[i])
        j=i+1
        while(j<len(n)):
        #for j in range(i+1,len(n)):
            #print (n[j])
            curr_sum = curr_sum + n[j]
            #print(curr_sum)
            if(curr_sum==sum):
                print ("Sum found between indexes",( i, j)) 
            if (curr_sum > sum or j == n):
                break

            j += 1


n = [23,56,4,8,67,56,90,123]
sum = 135
find_subarray_sum(n,sum)

Output:--
Sum found between indexes (1, 4)
Sum found between indexes (2, 5)
