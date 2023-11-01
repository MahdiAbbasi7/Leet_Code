# in-place technique is very useful and  
# It is this technique of working directly in the input Array, and not creating a new Array,
# that we call in-place.


class Soulothin:
    def inpalce(self, arr:list[int]) :
        # result = [] we don't need this because we want to use in-place technique;
        if len(arr) == 0 :
            print('false')
        for i in range(0, len(arr)) : 
            if i % 2 == 0 :
                arr[i] *= arr[i] 
        print(arr)

test = Soulothin()
test.inpalce(arr = [9, -2, -9, 11, 56, -12, -3])