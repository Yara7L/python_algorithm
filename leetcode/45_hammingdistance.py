# 两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
#
# 给出两个整数 x 和 y，计算它们之间的汉明距离。
#
# 注意：
# 0 ≤ x, y < 231.
#
# 示例:
# 输入: x = 1, y = 4
# 输出: 2
#
# 解释:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# 上面的箭头指出了对应二进制位不同的位置。

class Solution(object):
    def hammingdistance(self, x, y):
        """
        :param x: int
        :param y: int
        :return: int
        """
        if 0 < x < 231 and 0 < y < 231:
            return bin(x ^ y).count('1')
        else:
            return 0

    def hammingdistance2(self, x, y):
        """
       :param x: int
       :param y: int
       :return: int
       """
        z = x ^ y
        count = 0
        while z != 0:
            if z & 1 == 1:
                count += 1
            z = z >> 1
        return count

    def hammingdistance3(self, x, y):
        """
        :param x: int
        :param y: int
        :return: int
        """
        count = 0
        z = x ^ y
        while z != 0:
            count += 1
            z = z & (z - 1)
        return count


if __name__ == "__main__":
    test = Solution()
    print(test.hammingdistance(8, 23))
    print(test.hammingdistance2(8, 4))
    print(test.hammingdistance3(8,23))
