# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution(object):
    def generate(self, num):
        """
        :param num: int
        :return: list[lis[int]]
        """
        tri = []
        l = [1]
        for i in range(num):
            tri.append(l)
            l = [sum(t) for t in zip([0] + l, l + [0])]
        return tri

    def generate2(self, num):
        """
        :param num: int
        :return: list[lis[int]]
        """
        if num == 0:
            return []
        if num == 1:
            return [[1]]
        res = [[1][1, 1]]
        for i in range(2, num):
            a = [0] * (i + 1)
            a[0], a[i] = 1, 1
            for j in range(1, i):
                a[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(a)
        return res


if __name__ == "__main__":
    test = Solution()
    print(test.generate(5))
    print(test.generate(5))
