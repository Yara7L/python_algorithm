# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
#
# 示例:
# 输入: 11
# 输出: 3
# 解释: 整数11的二进制表示为00000000000000000000000000001011
#
# 示例2:
# 输入: 128
# 输出: 1
# 解释: 整数128的二进制表示为00000000000000000000000010000000

class Solution(object):
    def hammingWeight(self, num):
        """
        :param num: int
        :return: int
        """
        count = 0
        while num != 0:
            if num & 1 == 1:
                count += 1
            num = num >> 1
        return count

    def hammingWeight2(self, num):
        """
        :param num:int
        :return: int
        """
        if num == 0:
            return 0
        if num == 1:
            return 1
        m = num // 2
        k = num % 2
        return k + self.hammingWeight2(m)


if __name__ == "__main__":
    test = Solution()
    print(test.hammingWeight(11))
    print(test.hammingWeight2(11))
