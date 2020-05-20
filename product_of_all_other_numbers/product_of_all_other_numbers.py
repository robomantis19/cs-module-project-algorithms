'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    ret_arr = []
    new_arr = []
    if len(arr) == 2: 
        ret_arr.append(arr[1])
        ret_arr.append(arr[0])
        return ret_arr
    for i in range(0, len(arr)): 
        not_it = arr[i]
        for j in arr:
            if j != not_it: 
                new_arr.append(not_it)
        product = 1
        for p in new_arr: 
            product *= p
        ret_arr.append(product)
    print(ret_arr)
        

    #this code didn't work try popping it and multiplying values next time.


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
