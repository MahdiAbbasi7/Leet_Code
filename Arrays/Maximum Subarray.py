'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

'''
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if max(nums) < 0:
            return max(nums)
            
        max_so_far = 0
        max_ending_here = 0

        for i in range(0, len(nums)):
            if max_ending_here < 0:
                max_ending_here = 0
            max_ending_here = max_ending_here + nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

        return max_so_far

instance = Solution()
print(instance.maxSubArray([-3,-2,-2,-3]))