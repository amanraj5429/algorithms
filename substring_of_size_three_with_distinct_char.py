'''
A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
'''

def sub_size_three(s):
    subs = []
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            subs.append(sub)
    
    len_three_sub = [i for i in subs if len(i) == 3 and len(set(i)) == 3]
    return len(len_three_sub)

if __name__ == '__main__':
    s = "xyzzaz"
    ans = sub_size_three(s)
    print(ans)