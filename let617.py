# 617. Merge Two Binary Trees
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 is not None and t2 is not None:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
        elif t1 is None and t2 is not None:
            t1 = t2
        return t1

t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

t2 = TreeNode(2)
t2.right = TreeNode(3)
t2.right.right = TreeNode(7)
t2.left = TreeNode(1)
t2.left.right = TreeNode(4)

t = Solution().mergeTrees(t1, t2)

