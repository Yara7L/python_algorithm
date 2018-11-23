# 给定一个二叉树，返回其节点值的锯齿形层次遍历。
# （即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

class TreeNode(object):
    def __init__(self, root):
        self.value = root
        self.lchild = None
        self.rchild = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :param TreeNOde: TreeNode
        :return: list[list[int]]
        """
        res = []
        if not root:
            return res
        stack = [root]  # 保存每一层的节点
        yy = []
        k = 0  # 判断是奇数层还是偶数层
        while stack:
            k += 1
            y = []
            l = len(stack)
            for i in range(l):
                cur = stack.pop(0)
                y.append(cur.value)
                if cur.lchild:
                    stack.append(cur.lchild)
                if cur.rchild:
                    stack.append(cur.rchild)
            if k % 2 == 1:
                yy.append(y)
            else:
                yy.append((y[::-1]))
        return yy


if __name__ == "__main__":
    test = Solution()
    root = TreeNode(1)
    root.lchild = TreeNode(2)
    root.rchild = TreeNode(3)
    root.lchild.lchild = TreeNode(4)
    root.lchild.rchild = TreeNode(5)
    root.rchild.lchild = TreeNode(6)
    root.rchild.rchild = TreeNode(7)
    print(test.zigzagLevelOrder(root))
