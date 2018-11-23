# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# [3, 9, 20, 15, 7],  [9, 3, 15, 20, 7]
# 先序遍历： 根-》左子树-》右子树
# 中序遍历： 左子树-》根-》右子树
# 后序遍历： 左子树-》右子树-》根

class TreeNode(object):
    def __init__(self, root):
        self.value = root
        self.lchild = None
        self.rchild = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :param preorder: list[int]
        :param inorder: list[int]
        :return: TreeNode
        """
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        index = inorder.index(root.value)
        leftlist, rightlist = [], []
        for n in preorder:
            if n in inorder[:index]:
                leftlist.append(n)
            elif n in inorder[index + 1:]:
                rightlist.append(n)
        # lenright = len(inorder) - index - 1
        root.lchild = self.buildTree(leftlist, inorder[: index])
        root.rchild = self.buildTree(rightlist, inorder[index + 1:])

        return root

    def buildTree2(self, preorder, inorder):
        """
        :param preorder: list[int]
        :param inorder: list[int]
        :return: TreeNode
        """
        if inorder == []:
            return None
        root = TreeNode(preorder[0])
        x = inorder.index(root.value)  # 找到根在中序中的位置
        root.left = self.buildTree2(preorder[1:x + 1], inorder[0:x])
        root.right = self.buildTree2(preorder[x + 1:], inorder[x + 1:])
        return root


if __name__ == "__main__":
    test = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9,  3, 15, 20, 7]
    print(test.buildTree(preorder, inorder))
    print(test.buildTree2(preorder, inorder))
