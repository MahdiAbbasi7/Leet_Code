'''
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

'''

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
        #nums = [-1,0,1,2,-1,-4]
def threeSum(nums):
        nums.sort() # [-4,-1,-1,0,1,2]
        result = []
        
        for i in range(len(nums) - 2): # -2 for last two numbers.
            if i > 0 and nums[i] == nums[i - 1]: # check duplicated.
                continue
            
            if nums[i] > 0 :
                 break
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1 # the num is duplicated. and go back to line 23
                elif nums[left] + nums[right] < -nums[i]:
                    left += 1
                else:
                    right -= 1
        
        return result

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums)) # [[-1,-1,2],[-1,0,1]]