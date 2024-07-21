'''
    Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true
    Example 2:

    Input: s = "rat", t = "car"
    Output: false
'''


class Solution:
    '''
    This class contains a method to check if two strings are anagrams of each other.
    '''

    def is_angram(self, s:str, t:str) -> bool:
        '''
        rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.
        '''
        hash_s = {}
        hash_t = {}
        s, t = list(s), list(t)

        for _, v in enumerate(s):
            if v in hash_s:
                hash_s[v] += 1
            else:
                hash_s[v] = 1

        for _, v in enumerate(t):
            if v in hash_t:
                hash_t[v] += 1
            else:
                hash_t[v] = 1

        return hash_s == hash_t

obj = Solution()
print(obj.is_angram("a", "a"))
