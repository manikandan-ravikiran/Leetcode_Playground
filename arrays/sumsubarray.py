class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        startsum = {0: 1}
        s = 0
        result = 0
        for i in nums:
            s += i
            result += startsum.get(s - k, 0)
            startsum[s] = startsum.get(s, 0) + 1
        return result