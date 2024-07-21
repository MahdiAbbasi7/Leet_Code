class Solution:
    '''
    Example 1:

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

    Example 3:

        Input: nums = [3,3], target = 6
        Output: [0,1]

    '''
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        '''  target - hash[x] = hash[x+1] '''
        hash_nums = {}
        for k, v in enumerate(nums):
            if v in hash_nums:
                return [hash_nums[v], k]
            else:
                hash_nums[target - v] = k


        print(hash_nums)

obj = Solution()
print(obj.two_sum([3,2,4], 6))
