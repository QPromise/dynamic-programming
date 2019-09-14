# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return
        queue=[]
        queue.append(root)
        x_root=TreeNode(0)
        y_root=TreeNode(0)
        deep,deep_x,deep_y=0,0,0
        while len(queue) > 0:
            deep+=1
            temp=[]
            for node in queue:
                if node.left is not None:
                    temp.append(node.left)
                    if node.left.val == y:
                        y_root=node
                        deep_y=deep
                    if node.left.val == x:
                        x_root=node
                        deep_x=deep
                if node.right is not None:
                    temp.append(node.right)
                    if node.right.val == y:
                        y_root=node
                        deep_y=deep
                    if node.right.val == x:
                        x_root=node
                        deep_x=deep
            queue=temp
        print(deep_x,deep_y)
        return x_root.val != y_root.val and deep_x == deep_y