'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    #two pointers, index and k
    #for each item look ahead until k saving the highest value
    res = []
    end = len(nums) - k+ 1
    for i in range(end):
        max = nums[i]
        for j in range(i, k+i if k+i < len(nums) else len(nums)):
            if nums[j] > max:
                max = nums[j]
        res.append(max)
    return res

    




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
