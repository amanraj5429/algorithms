'''
Geeks For Geeks Problem

Given a string S. The task is to find the first repeated character in it. 
We need to find the character that occurs more than once and whose index of second occurrence is smallest. S contains only lowercase letters.

If no char repeated return -1.
'''


def repeat_char(S):
    ans = []
    for i in S:
        if i not in ans:
            ans.append(i)
        else:
            return i