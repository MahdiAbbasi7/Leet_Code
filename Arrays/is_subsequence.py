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

        t_index = 0
        for char in s:
            while t_index < len(t) and t[t_index] != char:
                t_index += 1
            if t_index == len(t):
                return False
            t_index += 1
        return True



obj = Solution()
print(obj.is_subsequence(s = 'ahc', t = "ahbgdc"))
