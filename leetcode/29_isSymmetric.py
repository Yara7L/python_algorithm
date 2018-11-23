# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# 说明:
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :param root: TreeNode
        :return: bool
        """

        def issametree(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return issametree(l.left, r.right) and issametree(r.left, l.right)
            else:
                return False

        if not root:
            return True
        print(issametree(root.left, root.right))
        return issametree(root.left, root.right)


if __name__ == "__main__":
    root = TreeNode(int(1))
    root.left = TreeNode(int(2))
    root.right = TreeNode(int(3))
    root.left.left = TreeNode(int(4))
    root.left.right = TreeNode(int(5))
    test = Solution()
    test.isSymmetric(root)
