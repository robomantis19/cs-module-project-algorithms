'''
Input: a List of integers
Returns: a List of integers
'''
# I will iterate through the array
# move the index from range(0:current) = beginning

def moving_zeroes(arr):
    # Your code here

    for i in range(0, len(arr)): 
        if arr[i] == 0: 
            zero = i
        else: 
            nonzero = i
            if nonzero != None: 
                while zero < nonzero:
                    arr[zero], arr[nonzero] = arr[nonzero], arr[zero]
        if arr[i+1] != 0: 
            nonzero2 = i+1
            while zero2 < nonzero2: 
                arr[zero2], arr[nonzero2] = arr[nonzero2], arr[zero2]
        else: 
            zero2 = i+1
        
        
    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")