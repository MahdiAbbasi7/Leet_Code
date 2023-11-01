class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        for i in range(0, len(arr)):
            if i == len(arr) - 1 :
                arr.pop(i)
                arr.append(-1)
        # print(arr)
        # todo: other tasks



test = Solution()
test.replaceElements(arr = [1])   

list = [1, 2, 3, 4, 5, 6, 7]
print(list[2:])