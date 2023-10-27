'''
Input: nums = [4,1,2,1,2]
Output: 4
'''

def single_num(nums):
    s = set()

    for i in nums:
        if i in s:
            s.remove(i)
        else:
            s.add(i)

    for j in s:
        return j        
    

if __name__ == '__main__':
      nums = [4,1,2,1,2]
      answer = single_num(nums)
      print(answer)