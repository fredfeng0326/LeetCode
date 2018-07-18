# 821. Shortest Distance to a Character


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        list_c = []
        for index,item in enumerate(S):
            if C == item:
                list_c.append(index)
        list_return = []
        for index,item in enumerate(S):
            list_dif = []
            for dif in list_c:
                list_dif.append(abs(index - dif))
            list_return.append(min(list_dif))
        return list_return

    def shortestToChar2(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        list_c = []
        for index, item in enumerate(S):
            if C == item:
                list_c.append(index)
        list_return = []
        for index, item in enumerate(S):
            distance = [abs(index - index_list) for index_list in list_c]
            list_return.append(min(distance))
        return list_return


a = Solution()
print(a.shortestToChar('loveleetcode','e'))