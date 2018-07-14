class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        r_list = []
        for item in nums1:
            r_list.append(next((j for j in nums2[nums2.index(item):] if j > item),-1))
        return r_list

a = Solution()
print (a.nextGreaterElement([2,4],[1,2,3,4]))
