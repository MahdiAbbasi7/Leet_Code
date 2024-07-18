class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        j = n + m - 1

        while j >= 0:
            if i2 >= 0 and (m == 0 or nums2[i2] >= nums1[i1]):
                nums1[j] = nums2[i2]
                i2 -= 1
            elif i2 > -1 and nums1[i1] > nums2[i2]:
                nums1[j], nums1[i1] = nums1[i1], nums1[j]
                if i1: i1 -= 1            
            j -= 1

        if i2 > -1:
            for i in range(i2 + 1):
                nums1[i] = nums2[i]
    
test = Solution()
test.merge([1,2,3,0,0,0],3,[2,5,6],3)