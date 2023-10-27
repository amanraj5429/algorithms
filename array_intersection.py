'''
problem- leetcode
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note order doesn't matter
'''

def intersection(nums1, nums2):
    ans = []
    for i in nums1:
        if i in nums2:
            ans.append(i)

    return ans

if __name__ == '__main__':
    result = intersection([4,9,5], [9,4,9,8,4])
    print(result)