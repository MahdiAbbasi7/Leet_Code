# Input: nums = [3,1,2,4]
# Output: [2,4,3,1], [4,2,3,1], [2,4,1,3], and [4,2,1,3]

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even = []
        odd = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        res = list(even + odd)
        print (res)


test =  Solution()
test.sortArrayByParity([3,4,2,4, 3])