'''
Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".
'''

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x = sorted(s, reverse=True)
        for i in range(len(x)-1, -1, -1):
            x[i], x[-1] = x[-1], x[i]
            break
        return ''.join(x)

instance = Solution()
print(instance.maximumOddBinaryNumber("0101"))