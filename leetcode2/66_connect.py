# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
# 如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
# 示例:
#
# 给定完美二叉树，
#
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# 调用你的函数后，该完美二叉树变为：
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL
# 说明:
# 你只能使用额外常数空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
# 你可以假设它是一个完美二叉树（即所有叶子节点都在同一层，每个父节点都有两个子节点）。

class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        """
        层次遍历，连接每一层的节点
        :param root: TreeLinkNode
        :return:
        """
        if not root:
            return
        stack = [root]
        while stack:
            l = len(stack)
            for i in range(l):
                cur = stack.pop(0)
                if i < l - 1:
                    cur.next = stack[0]
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                    # print(cur.val,cur.next)

        return

    def connect2(self, root):
        """
        迭代
        :param root: TreeLinkNode
        :return:
        """
        if root and root.left:
            # exist left and right tree
            # connect the right to the left
            # 完美二叉树，有左子树必有右子树
            root.left.next = root.right
            if root.next:
                # 如果该节点的next指针指向的节点不为None，则指向next指向的节点的左子树
                root.right.next = root.next.left
            else:
                root.right.next = None
            self.connect2(root.left)
            self.connect2(root.right)


if __name__ == "__main__":
    test = Solution()
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.left = TreeLinkNode(4)
    root.right.right = TreeLinkNode(5)
    test.connect(root)
    test.connect2(root)

