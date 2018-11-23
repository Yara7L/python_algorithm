# 给出一个整数，写一个函数来确定这个数是不是3的一个幂。
#
# 后续挑战：
# 你能不使用循环或者递归完成本题吗？

# 如果该数能被3的n次方的最大整数整除，被该数即为3的幂。
class Solution(object):
    def isPowerOfThree(self, num):
        """
        :param num:int
        :return: bool
        """
        if num < 3:
            return False
        return 1162261467 % num == 0 and num > 2

    def isPowerOfThree(self,num):
        """
        :param num:int
        :return: bool
        """
        import math
        if 3**(round(math.log(num,3)))==num:
            return True
        else:
            return False


if __name__ == "__main__":
    test = Solution()
    print(test.isPowerOfThree(27))
    print(test.isPowerOfThree(27))
