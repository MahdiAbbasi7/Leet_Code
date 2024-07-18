# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]

# ----------------------------

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        sorted_list = sorted(heights)
        counter = 0
        for i in range(len(sorted_list)):
            if sorted_list[i] != heights[i]:
                counter += 1
        print(sorted_list)
        print(counter)

test = Solution()
test.heightChecker([5,1,2,3,4])