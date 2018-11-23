# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :param root: TreeNode
        :return:list[list[int]
        """
        if root is None:
            return []
        stack = [root]
        yy = []
        while stack:
            print(stack)
            y = []
            l = len(stack)
            for i in range(l):
                cur = stack.pop(0)
                y.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            yy.append(y)
        print(yy)
        return yy

    def levelOrder_2(self,root):
        """
        :param root: TreeNode
        :return:list[list[int]
        """
        if not root:
            return []
        ret=[]
        curlist=[root]
        while curlist:
            ret.append([i.val for i in curlist])
            nextlist=[]
            for i in curlist:
                if i.left:
                    nextlist.append(i.left)
                if i.right:
                    nextlist.append(i.right)
            curlist=nextlist
        print(ret)
        return ret

if __name__ == "__main__":
    root=TreeNode(int(1))
    root.left=TreeNode(int(2))
    print(root.val)
    root.right=TreeNode(int(3))
    root.left.left=TreeNode(int(4))
    test=Solution()
    test.levelOrder(root)
    test.levelOrder_2(root)



