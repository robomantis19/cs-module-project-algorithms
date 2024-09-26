'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    def max(x): 
        m= None
        for i in range(0, len(x) - 1): 
            if i >= i+1: 
                m = x[i]
            else: 
                m = x[i+1]
        return m
    arr = [] 
    for i in range(0, len(nums) - k ): 
        arr.append(max(nums[i:i+k]))
    print(arr)
    return arr
    

    # I think with this my max function is messed up. 
    # That is all I have to say about that right now.
    # What i think is the  most important thing is constantly improving the code, syntax, style, and efficency,
    #$of the code.


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
