# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # recursive solution

    # find the min value of the BST
    def minValueNode(self, root):
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # base case
        if not root:
            return None
        # find the key that we want to delete
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # case 1: 0 or 1 child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # case 2: 2 children
                # find the minimum value on the right side of the node
                minNode = self.minValueNode(root.right)
                # the root is now changed to the minimum value since it satisfies all conditions of still being greater than the left side and also less than the right side
                root.val = minNode.val
                # delete the node that we used to make the new root
                root.right = self.deleteNode(root.right, minNode.val)
        return root
