class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums==[]:
            return False
        i=0
        max1=nums[i]
        while i<len(nums):
            if i>max1:
                break
            max1=max(nums[i]+i,max1)
            i+=1
        if i==len(nums):
            return True
        return False
        