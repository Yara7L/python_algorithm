# 给定一个二叉树，返回它的中序遍历。
#
# 示例:
#
# 输入: [1, null, 2, 3]
# 1
# \
# 2
# /
# 3
#
# 输出: [1, 3, 2]
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
class TreeNode(object):
    def __init__(self, root):
        self.value = root
        self.lchild = None
        self.rchild = None


count = 0


class Solution(object):
    def inorderTraversal(self, root):
        """
        :param root: TreeNode
        :return: list[int]
        """
        res = []
        global count
        if root is None:
            count += 1
            return res
        # list.extend(),操作对象是list,扩容，可能增加多个；
        # list.append(),element整体增加，增加一个
        res.extend(self.inorderTraversal(root.lchild))
        res.append(root.value)
        res.extend(self.inorderTraversal(root.rchild))
        print(count)
        return res


if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    rchild = TreeNode(2)
    rchild_lchild = TreeNode(3)
    root.rchild = rchild
    rchild.lchild = rchild_lchild
    print(test.inorderTraversal(root))
