# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res_list = []
        for i in nums:
            res = i * i
            res_list.append(res)
            res_list.sort()
        print(res_list)




test = Solution()
test.sortedSquares([-7,-3,2,3,11])
