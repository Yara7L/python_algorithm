# 给定一个二叉树，找出其最大深度。
#
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最大深度 3 。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :param root: TreeNode
        :return: int
        """
        if not root:
            return 0
        else:
            l = 1 + self.maxDepth(root.left)
            r = 1 + self.maxDepth(root.right)
        # print(max(l, r))
        return max(l, r)


if __name__ == "__main__":
    root = TreeNode(int(1))
    root.left = TreeNode(int(2))
    root.right = TreeNode(int(3))
    root.left.left = TreeNode(int(4))
    root.left.right = TreeNode(int(5))
    test = Solution()
    test.maxDepth(root)
    print(test.maxDepth(root))
