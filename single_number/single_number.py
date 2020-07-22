'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    sorted = selection_sort(arr)
    for i in range(0,len(sorted),2):
        if sorted[i] is not sorted[i+1]:
            return sorted[i]

def selection_sort(arr):
    for i in range(0, len(arr)):
        low = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[low]:
                low = j
        temp = arr[i]
        arr[i] = arr[low]
        arr[low] = temp
    return arr



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")