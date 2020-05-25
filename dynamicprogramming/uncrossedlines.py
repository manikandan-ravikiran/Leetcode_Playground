class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [0] * (n + 1)
        for i in xrange(m):
            for j in range(n)[::-1]:
                if A[i] == B[j]: dp[j + 1] = dp[j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j + 1], dp[j])
        return dp[n]