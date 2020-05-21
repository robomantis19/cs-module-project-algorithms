'''
Input: an integer
Returns: an integer
'''

# 3 cookies

# 1 1 1
# 2 1
# 3

def eating_cookies(n):
    # Your code here

    if n == 0: 
        return 1
    elif n < 0: 
        return 0

    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)





    # if n == 0 or n == 1 : 
    #     return 1
    # total = 0
    # one = n/1
    # two = n/2
    # three = n/3
    # if n > 1: 
    #     stepTotal = one + two + three
    #     num = eating_cookies(stepTotal)     
    #     total += num
    
    # else: 
    #     return total

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
