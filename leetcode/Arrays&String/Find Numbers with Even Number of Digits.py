class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if (9 < nums[i] < 100) or (999< nums[i]< 10000) or (nums[i]==100000): 
                count += 1
        print(count)
                

test = Solution()
test.findNumbers([12,34,2,6,7896])