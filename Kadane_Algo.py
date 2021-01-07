from sys import maxsize 
def maxSubArraySum(a,size): 
  
    max_so_far = -maxsize - 1
    #print(max_so_far)
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
  
    for i in range(0,size): 
  
        max_ending_here += a[i]
        #print (max_ending_here)
  
        if max_so_far < max_ending_here:
            #print(max_so_far)
            max_so_far = max_ending_here
            #print(max_so_far)
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
  
    print ("Maximum contiguous sum is %d"%(max_so_far)) 
    print ("Starting Index %d"%(start)) 
    print ("Ending Index %d"%(end))

# Driver function to check the above function  
a = [1,2,3,-2,5]
maxSubArraySum(a,len(a)) 