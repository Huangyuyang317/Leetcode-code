class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def getk(k):
            index1=0
            index2=0
            while True:
                if index1==m-1:
                    return nums2[index2+k-1]
                if index2==n-1:
                    return nums1[index1+k-1]
                if k==1:
                    return min(nums1[index1],nums2[index2])
                pivot1=min(index1+k//2-1,m-1)
                # min是为了让指针的限制与移动后不至于超过某一个列表的边界
                pivot2=min(index2+k//2-1,n-1)
                if nums1[pivot1]>=nums2[pivot2]:
                    k-=pivot2-index2+1
                    index2=pivot2+1
                if nums1[pivot1]<nums2[pivot2]:
                    k-=pivot1-index1+1
                    index1=pivot1+1
                    


        m=len(nums1)
        n=len(nums2)
        l=m+n
        if l%2:
            return getk((l+1)/2)
        else:
            return (getk(l/2)+getk(l/2-1))/2