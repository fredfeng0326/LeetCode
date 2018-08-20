# 860. Lemonade Change
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        wallet = {5:0,10:0}
        for bill in bills:
            # 5
            if bill == 5:
                wallet[5] += 1
            elif bill == 10:
                if wallet[5] > 0:
                    wallet[10] += 1
                    wallet[5] -= 1
                else:
                    return False
            elif bill == 20:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -= 1
                    wallet[5] -=1
                elif wallet[5] >= 3:
                    wallet[5] -= 3
                else:
                    return False
        return True



