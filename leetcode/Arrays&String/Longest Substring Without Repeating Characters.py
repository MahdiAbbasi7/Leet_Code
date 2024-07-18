class Solution:
    def lengthOfLongesSubstring(self, s:str) -> int:
        res = 0
        p1 = 0
        seen = dict()
        for p2 in range(len(s)): 
            char = s[p2]
            if char in seen and seen[char] >= 1:
                p1 = seen[char] + 1
            else:
                result = max(result, p2 - p1 + 1)
            seen[char] = p2
        return res