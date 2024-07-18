class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1p = m - 1
        n2p = n - 1
        wp = m + n - 1

        while wp >= 0:
            if n1p ==0:
                ...
            if nums2[n2p] > nums1[n1p]:
                nums1[wp] = nums2[n2p]
                n2p -= 1
                wp -= 1
            else:
                nums1[wp] = nums1[n1p]
                n1p -= 1
                wp -= 1

    
test = Solution()
test.merge([1,2,3,0,0,0],3,[2,5,6],3)