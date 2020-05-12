class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        b, e = 0, len(nums) - 1
        while b < e:
            m = (b + e) // 2
            if m % 2 == 1 and nums[m - 1] == nums[m]:
                b = m + 1
            elif  m % 2 == 0 and nums[m + 1] == nums[m]:
                b = m + 2
            else:
                e = m
        return nums[b]