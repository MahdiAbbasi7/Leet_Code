'''
Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''


class Solution:
    '''Solution'''
    def is_subsequence(self, s: str, t: str) -> bool:
        '''sub'''
        l_s = list(s)
        l_t = list(t)

        for i in enumerate(l_s):
            for j in enumerate(l_t):
                if l_s[i] == l_t[j]:
                    i+=1
                j+=1
            return i == len(s)



obj = Solution()
print(obj.is_subsequence(s = 'abc', t = "ahbgdc"))
