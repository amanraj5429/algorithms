'''
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
'''


def check_panagrams(sentence):
    library = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    resultants = []
    for char in library:
        if char in sentence:
            resultants.append(1)
        else:
            resultants.append(0)
    
    if 0 in resultants:
        return False
    return True

if __name__ == '__main__':
    sentence = "thequickbrownfoxjumpsoverthelazydog"
    ans = check_panagrams(sentence)
    print(ans)