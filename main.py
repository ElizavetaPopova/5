class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a=nums1+nums2
        a.sort()
        n=len(a)
        if len(a)==0 or len(a)==1:
            return a[0]
        if n%2!=0:
            s=(n/2)
            return a[s]
        else:
            return (a[n/2]+a[(n/2)-1])/2.0
