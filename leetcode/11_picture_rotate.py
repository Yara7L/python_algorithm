# 给定一个 n × n 的二维矩阵表示一个图像。
# 将图像顺时针旋转 90 度。

# 说明：
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

# 示例 1:
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# 示例 2:
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

import numpy as np
class Solution:
    def picture_rotate(self,matrix):
        """
        :type matrix:list[list[int]]
        :rtype:none
        """

        # copy了一个矩阵，进行赋值，逐行交换，是原地旋转么？？
        new=matrix.copy()
        n=len(matrix)
        for i in range(n):
            # 每一列换乘每一行
            matrix[i]=[new[j][i] for j in range(n-1,-1,-1)]
            print(matrix)
        print(matrix)
        return

    # 转置后，左右交换位置
    def picture_rotate_2(self,matrix):
        """
        :type matrix:list[list[int]]
        :rtype:none
        """
        matrix[:] = map(list, zip(*np.asarray(matrix).T[: : ]))
        print(matrix)


if __name__=="__main__":
    test=Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    test.picture_rotate(matrix_2)
    test.picture_rotate_2(matrix_2)