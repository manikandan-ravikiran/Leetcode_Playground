class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res=[0]
        for i in xrange(1,num+1):
            res.append(res[i>>1]+(i&1))
        return res