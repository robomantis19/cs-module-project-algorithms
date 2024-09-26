'''
Input: a List of integers
Returns: a List of integers
'''
# I will iterate through the array
# move the index from range(0:current) = beginning

def moving_zeroes(arr):
    # Your code here
    left = 0 
    right = len(arr) - 1

    while left <= right: 
        if arr[left] == 0 and arr[right] != 0: 
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        else: 
            if arr[left] != 0: 
                left += 1
            if arr[right] == 0: 
                arr[right] -= 1
    return arr

    # for i in range(0, len(arr) -1 ): 
    #     if arr[i] == 0: 
    #         zero = i
    #     else: 
    #         nonzero = i
    #         if nonzero != None: 
    #             while arr[zero] < arr[nonzero]:
    #                 arr[zero], arr[nonzero] = arr[nonzero], arr[zero]

    #     if arr[i+1] != 0: 
    #         nonzero2 = i+1
    #         while arr[zero2] < arr[nonzero2]: 
    #             arr[zero2], arr[nonzero2] = arr[nonzero2], arr[zero2]
    #     else: 
    #         zero2 = i+1
        
        
    # return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")