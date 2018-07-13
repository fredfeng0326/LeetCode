# 575. Distribute Candies
class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        len1 = len(set(candies))
        if len1 > len(candies)/2:
            return int(len(candies)/2)
        else:
            return len1

    def distributeCandies2(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        sister_count = len(candies) // 2
        unique_candies = set(candies)
        return min(sister_count, len(unique_candies))

a = Solution()
print (a.distributeCandies([1,1,2,3]))