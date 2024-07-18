# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.



class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        print(max(nums))


test = Solution()
test.thirdMax([3,2,1])

