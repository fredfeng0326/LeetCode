# 728. Self Dividing Numbers

class Solution:
    def isDividingNumber(self, num):
        if '0' in str(num):
            return False
        else:
            return 0 == sum(num%int(i) for i in str(num))

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        list =[]
        for item in range(left,right+1,1):
            if self.isDividingNumber(item):
                list.append(item)
        return list

    def selfDividingNumbers2(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        is_self_dividing = lambda num: '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
        x = filter(is_self_dividing, range(left, right + 1))
        return list(x)


a = Solution()
print(a.selfDividingNumbers(1,22))
print(a.selfDividingNumbers2(1,22))