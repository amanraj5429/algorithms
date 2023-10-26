def int_concat(nums):

    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        n = len(nums)
        sum = 0
        for i in range(n):
            sum += nums[i]*(10**(n-i-1))
        return sum