# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def f(self, node, remainingsum, pathnodes, pathslist):
        if not node:
            return
        pathnodes.append(node.val)
        if remainingsum == node.val and not node.left and not node.right:
            pathslist.append(list(pathnodes))
        else:
            self.f(node.left, remainingsum-node.val, pathnodes, pathslist)
            self.f(node.right, remainingsum-node.val, pathnodes, pathslist)
        pathnodes.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        pathlist=[]
        self.f(root, targetSum, [], pathlist)
        return pathlist
        