'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    if len(arr) == 0:
        return arr
    i = 0
    j = len(arr) -1
    #if empty return arr
    while arr[j] == 0:
        if j == i:
            return arr
        j -= 1
    while i != j:
        if i == j or j < i:
            return arr
    #loop through arr
        if arr[i] == 0:
            arr[i] = arr[j]
            arr[j] = 0
            while arr[j] == 0:
                if j == i or j < i:
                    return arr
                j -= 1
        #if current_val is zero, swap places with valid-end
        #Find Valid end = start at end and decrement until find a non zero value
        #Swap current with valid end, find next valid end
        i += 1
        #j -= 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")