nums=nums1+nums2
nums.sort(reverse=True)
if nums%2:
    print(nums[len((nums-1)/2)])
else:
    print((nums[len((nums-1)/2)]+nums[len((nums+1)/2)])/2)
# 这个算法的时间复杂度为O((m+n)log(m+n)),这是排序的复杂度，合并的复杂度为O(m+n),所以最大的是O((m+n)log(m+n))