'''
Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true

Example 4:

Input: s = "badc", t = "baba"
Output: false

lens must be equal? no
one char may be map to itsel
no two char may be map to one char

'''

class Solution:
    '''solution'''
    def is_isomorphic(self, s: str, t: str) -> bool:
        ''' sample'''
        map1 = []
        map2 = []
        for idx in s:
            map1.append(s.index(idx))
        for idx in t:
            map2.append(t.index(idx))
        print(map1)
        print(map2)
        if map1 == map2:
            return True
        return False


obj = Solution()
print(obj.is_isomorphic(s = "egg", t = "add"))
