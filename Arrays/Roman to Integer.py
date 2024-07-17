'''
Symbol       Value
I             1
IV            4
V             5
IX            9
X             10
XL            40
L             50
XC            90
C             100
CD            400
D             500
CM            900
M             1000

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        ls = list(s) #"MCMXCIV"
        res = 0
        alphba = {
            'I'  : 1, 
            'V'  : 5, 
            'X'  : 10,
            'L'  : 50, 
            'C'  : 100,
            'D'  : 500,
            'M'  : 1000 }
        
        for i in range(len(ls)-1):
            if alphba[ls[i]] < alphba[ls[i+1]]:
                res -= alphba[ls[i]]
            else:
                res += alphba[ls[i]]

        return res + alphba[[ls[-1]]]


obj = Solution()
print(obj.romanToInt("MCMXCIV"))