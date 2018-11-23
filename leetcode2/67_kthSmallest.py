# 给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
#
# 说明：
# 你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
#
# 方案一：中序排序后，返回第K-1个值
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :param root: TreeNode
        :return: int
        """
        return self.inOrderTraversal(root)[k - 1]

    def inOrderTraversal(self, root):
        if root is None:
            return []
        res = []
        res.extend(self.inOrderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inOrderTraversal(root.right))
        return res


if __name__ == "__main__":
    test = Solution()
    # 要求树为，搜索二叉树；左子树（节点）小于根节点，根结点小于右子树，
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(test.inOrderTraversal(root))
    print(test.kthSmallest(root,5))
