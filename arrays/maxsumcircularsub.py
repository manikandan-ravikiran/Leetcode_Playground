class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # ans1: answer for one-interval subarray
        ans1 = cur = None
        for x in A:
            cur = x + max(cur, 0)
            ans1 = max(ans1, cur)

        # ans2: answer for two-interval subarray, interior in A[1:]
        ans2 = cur = float('inf')
        for i in xrange(1, len(A)):
            cur = A[i] + min(cur, 0)
            ans2 = min(ans2, cur)
        ans2 = sum(A) - ans2

        # ans3: answer for two-interval subarray, interior in A[:-1]
        ans3 = cur = float('inf')
        for i in xrange(len(A)-1):
            cur = A[i] + min(cur, 0)
            ans3 = min(ans3, cur)
        ans3 = sum(A) - ans3
        
        return max(ans1, ans2, ans3)