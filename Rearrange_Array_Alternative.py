#Given a sorted array of positive integers, rearrange the array alternately i.e first element should be maximum value,
#second minimum value, third second max, fourth second min and so on. 

def rearrange(arr, N):
    temp = N*[None]
    small, large = 0, N-1
    flag = True

    for i in range(N):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1

        flag = bool(1-flag)

    for i in range(N):
        arr[i] = temp[i]
    return arr

# Driver code
arr = [1, 2, 3, 4, 5, 6]
N = len(arr)
print("Original Array")
print(arr)
print("Modified Array")
print(rearrange(arr, N))

#Output
#Original Array
#[1, 2, 3, 4, 5, 6]
#Modified Array
#[6, 1, 5, 2, 4, 3]
