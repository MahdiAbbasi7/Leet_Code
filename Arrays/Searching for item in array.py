class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        count=0
        for i in arr:
            if(i*2 in arr and i!=0):
                return True
            if(i==0):
                count+=1
        if(count>1):
            return True
            
        return False

test = Solution()
test.checkIfExist([10,2,5,3])