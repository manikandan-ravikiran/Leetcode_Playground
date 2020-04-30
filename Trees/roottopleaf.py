# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root,pos):
            if not root or root.val!=arr[pos]:
                return False
            if pos == len(arr)-1:
                return not root.left and not root.right
            return dfs(root.left,pos+1) or dfs(root.right,pos+1)
        
        return dfs(root,0)