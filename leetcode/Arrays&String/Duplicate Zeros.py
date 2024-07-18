# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Input: arr = [1,2,3]
# Output: [1,2,3]
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        result = []
        for i in arr:
            result.append(i)
            if i == 0:
                result.append(i)
        for i in range(len(arr)):
            arr[i] = result[i]


test = Solution()
test.duplicateZeros([1,0,2,3,0,4,5,0])