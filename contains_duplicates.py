'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

def duplicates(nums):
    counter = {}
    for i in nums:
        if i not in counter:
            counter[i] = 0
        counter[i] += 1
    if max(counter.values()) == 1:
        return False
    return True