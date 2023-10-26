def int_concat(nums):
    n = len(nums)
    sum = 0
    for i in range(n):
        sum += nums[i]*(10**(n-i-1))
    return sum