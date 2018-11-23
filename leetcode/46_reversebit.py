# 颠倒给定的 32 位无符号整数的二进制位。
#
# 示例:
#
# 输入: 43261596
# 输出: 964176192
# 解释: 43261596 的二进制表示形式为 00000010100101000001111010011100 ，
#      返回 964176192，其二进制表示形式为 00111001011110000010100101000000 。
# 进阶:
# 如果多次调用这个函数，你将如何优化你的算法？

class Solution(object):
    def reversebit(self, num):
        """
        :param num:int
        :return: int
        """
        # for i in range(0,16):
        #     num=num<<i
        return int(bin(num)[2:][::-1] + '0' * (32 - len(bin(num)[2:])), 2)

    def reversebit2(self, num):
        r = bin(num)[:: -1][: -2]
        while len(r) < 32:
            r += '0'
        return int(r, 2)

    def reversebit3(self, num):
        res = 0
        for i in range(0, 32):
            res = res << 1
            res = res | (num & 1)
            num = num >> 1
        return res
# 循环交换位，第i位与第32-i位

if __name__ == "__main__":
    test = Solution()
    print(test.reversebit(12394))
    print(test.reversebit2(12394))
    print(test.reversebit3(12394))
