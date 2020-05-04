class Solution:
    def findComplement(self, num: int) -> int:
        P = 2
        while P<=num:
            P*=2
        return P-1-num