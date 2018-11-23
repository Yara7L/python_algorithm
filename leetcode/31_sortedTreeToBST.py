# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定有序数组: [-10,-3,0,5,9],
#
# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def sortedArrayToBST(self,nums):
        """

        :param nums: list[int]
        :return: TreeNode
        """
        if not num:
            return

        mid=len(nums)//2
        root=TreeNode(nums[mid])
        left=nums[:mid]
        right=nums[mid+1:]
        root.left=self.sortedArrayToBST(left)
        root.right=self.sortedArrayToBST()(right)
        return root

if __name__=="__main__":
    pass