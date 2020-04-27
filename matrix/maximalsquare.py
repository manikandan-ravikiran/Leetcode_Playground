class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n, max_len = len(matrix), len(matrix[0]), 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
                    max_len = max(max_len, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0
        return max_len * max_len