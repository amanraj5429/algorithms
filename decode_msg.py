'''
You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').


Input: key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"
Output: "this is a secret"
Explanation: The diagram above shows the substitution table.
It is obtained by taking the first appearance of each letter in "the quick brown fox jumps over the lazy dog".

'''

def decode_msg(key, msg):
    lst = []
    d_list = key.split(" ")
    for words in d_list:
        for word in words:
            if word in lst:
                continue
            else:
                lst.append(word)

    ans = []
    library = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    msg_list = msg.split(" ")
    for words in msg_list:
        c = ''
        for word in words:
            d=library[(lst.index(word))]
            c+=d
        ans.append(c)
    return " ".join(ans)

if __name__ == '__main__':
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    ans = decode_msg(key, message)
    print(ans)