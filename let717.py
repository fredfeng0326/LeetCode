class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        length = len(bits)
        dot = 0
        while dot < length:
            if dot == length -1:
                return True
            if bits[dot] == 0:
                dot += 1
            else:
                dot += 2
        return False