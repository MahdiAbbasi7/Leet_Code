class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums_test = list(set(nums))
        print (nums_test)
    
test = Solution()
test.removeDuplicates([0,0,1,1,1,2,2,3,3,4])