'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    dictionary = {}
    for i in arr: 
        dictionary[f'{i}'] = 0
    for i in range(len(arr)):
        dictionary[f'{arr[i]}'] += 1 
        
    for key, value in dictionary.items(): 
        if value == 1: 
            return int(key)
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")