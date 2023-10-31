'''
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
'''



def find_third_max(nums):
    first_max = second_max = third_max = float('-inf')
    unique_nums = []
    for i in nums:
        if i not in unique_nums:
            unique_nums.append(i)

    for num in unique_nums:
        if num > first_max:
            third_max = second_max
            second_max = first_max
            first_max = num
        elif num > second_max:
            third_max = second_max
            second_max = num
        elif num > third_max:
            third_max = num

    return third_max if len(unique_nums) >= 3 else first_max