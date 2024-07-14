nums1, nums2 = [1, 2], [3, 4]



res = sorted(nums1 + nums2)

print(res)
if len(res) % 2 == 1 :
    print (res[len(res) // 2])

# [1, 2, 3, 4]

if len(res) % 2 == 0 :
    final = res[(len(res) - 1 ) // 2] + res[(len(res) // 2)]
    print (final / 2)

## binary search - DC