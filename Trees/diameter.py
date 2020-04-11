class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.sol = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.sol = max(self.sol, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.sol - 1