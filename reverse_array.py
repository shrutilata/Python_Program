#Source Code:--

def Reverse_array(n):
    l=[]
    for i in range(0,n):
        a=int(input("Enter the elements:--"))
        l.append(a)
    print("The reversed array is",*l[::-1])     

#Driver Code:--
Reverse_array(7)

#Output

Enter the elements:--1
Enter the elements:--2
Enter the elements:--3
Enter the elements:--4
Enter the elements:--5
Enter the elements:--6
Enter the elements:--7
    
The reversed array is 7 6 5 4 3 2 1
