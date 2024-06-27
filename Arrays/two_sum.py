
'''
nums = [11,11,7,2], target = 9
output = [0,3]
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index, number in enumerate(nums):
            for j in range(index + 1,len(nums)):
                if number + nums[j] == target :
                    return [index, j]


test = Solution()
print(test.twoSum([11,11,7,2], 9))