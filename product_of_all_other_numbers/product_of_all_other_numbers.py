'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    #create hash table with the number of occurances
    lookup = {}
    for i in range(len(arr)):
        if arr[i] in lookup.keys():
            lookup[arr[i]] += 1
        else:
            lookup[arr[i]] = 1
    #loop through array
    for i in range(len(arr)):
        sum = 1
        for k, v in lookup.items():
            if k == arr[i]:
                if lookup[k] == 1:
                    pass
                else:
                    sum = sum * k**(v-1)
            else:    
                sum = sum * k**v
        arr[i] = sum
    #for each number multiply all of the keys to the power of the value
    #except for the key that matches current pos
    #if value is 1 then use 1, else reduce power by one
    return arr


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
