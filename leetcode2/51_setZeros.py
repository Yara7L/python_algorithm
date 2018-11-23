# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
# 示例 1:
# 输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# 示例 2:
# 输入:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# 进阶:
# 一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个常数空间的解决方案吗？
import copy


class Solution(object):
    def setZeros(self, nums):
        """
        O(m*n)
        :param nums: list[list[int]]
        :return: list[list[int]]
        """
        res = copy.deepcopy(nums)
        a = len(nums)
        b = len(nums[0])
        for i in range(a):
            for j in range(b):
                if nums[i][j] == 0:
                    res[i] = [0] * b
                    for k in range(a):
                        res[k][j] = 0
        return res

    def setZeros2(self, nums):
        """
        :param nums: list[list[int]]
        :return: list[list[int]]
        """
        index = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] == 0:
                    index.append((i, j))
        for i, j in index:
            nums[i] = [0] * len(nums[i])
            for k in range(len(nums)):
                nums[k][j] = 0
        return nums


if __name__ == "__main__":
    test = Solution()
    nums = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    print(test.setZeros(nums))
    print(nums)
    print(test.setZeros2(nums))
