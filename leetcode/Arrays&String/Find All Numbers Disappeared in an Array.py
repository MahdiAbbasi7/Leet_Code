# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums.sort()
        nums = set(nums)
        new_list = []
        for i in range(1,len(nums)+1):
            new_list.append(i)
            i+=1
        result = list(set(new_list) - nums)
        return result

        # print (list((set(range(1, len(nums) + 1)) - set(nums))))

test = Solution()
print(test.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
        