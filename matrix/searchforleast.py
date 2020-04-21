# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        norow=binaryMatrix.dimensions()[0]-1
        nocol=binaryMatrix.dimensions()[1]-1
        row=0
        col=nocol
        
        
        while row<=norow and col>=0:
            if binaryMatrix.get(row, col)==1:
                col-=1
            else:
                row+=1
        
        if col ==nocol:
            return -1
        else:
            return col+1