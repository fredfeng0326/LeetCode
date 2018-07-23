# 784. Letter Case Permutation

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        rlist = [S]
        for i,item in enumerate(S):
            if not item.isalpha():
                continue
            l_new = []
            for strings in rlist:
                swap_str = (strings[:i] + strings[i].swapcase() + strings[i + 1:])
                print(swap_str)
                l_new.append(swap_str)
            rlist.extend(l_new)
        return rlist

    def letterCasePermutation2(self, S):
        ans = []

        def dfs(S, i, n):
            if i == n:
                ans.append(''.join(S))
                return

            dfs(S, i + 1, n)
            if not S[i].isalpha(): return
            S[i] = S[i].swapcase()
            dfs(S, i + 1, n)
            S[i] = S[i].swapcase()

        dfs(list(S), 0, len(S))
        return ans
a = Solution()
print (a.letterCasePermutation('a1b2'))
print (a.letterCasePermutation2('a1b2'))