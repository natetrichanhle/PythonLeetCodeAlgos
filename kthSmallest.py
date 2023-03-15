# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative solution 
        visited = 0
        stack = []
        cur = root

        while cur or stack:
            # search left subtree
            while cur:
                stack.append(cur)
                cur = cur.left
                 
            # once it's popped, we know that it was visited already
            cur = stack.pop()
            visited += 1
            if visited == k:
                return cur.val
            # search right subtree
            cur = cur.right