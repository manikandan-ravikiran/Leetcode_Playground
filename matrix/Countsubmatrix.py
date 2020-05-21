class Solution(object):
    def countSquares(self, A):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        for i in xrange(1, len(A)):
            for j in xrange(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return sum(map(sum, A))