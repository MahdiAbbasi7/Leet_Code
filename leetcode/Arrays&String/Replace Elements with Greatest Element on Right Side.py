class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # for i in range(0, len(arr)):
        mx = -1
        for i in range(len(arr) - 1, -1 , -1):
            arr[i], mx = mx, max(mx, arr[i])
        print (arr)
        



test = Solution()
test.replaceElements(arr = [17,18,5,4,6,1])   