# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

def product_except_self(nums):
    res = [1] * len(a)
    
    prod = 1
    for i in range(len(a)):
        res[i] = prod
        prod *= a[i]

    prod = 1
    for i in range(len(a)-1, -1, -1):
        res[i] *= prod
        prod *= a[i]
        
    return res

print(product_except_self([1,2,3,4]))
print(product_except_self([2,3,1]))
print(product_except_self([0,0,9,0,0]))
