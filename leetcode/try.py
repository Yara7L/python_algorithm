# 验证给定的字符串是否为数字。
#
# 例如:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
#
# 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。

# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
#      由于返回类型是整数，小数部分将被舍去。
class Solution(object):
    def test(self, s):
        """
        :param x: s
        :return:  int
        """
        s = s.lstrip()
        if s == '':
            return 0
        s_new = ''
        if s[0] == '-' or s[0] == '+':
            s_new += s[0]
            s = s[1:]
        else:
            s = s[:]

        for ch in s:
            if ch.isdigit():
                s_new += ch
            else:
                break
        if s_new.lstrip('+-').isdigit():
            s_new = int(s_new)
        else:
            return 0

        return min(2 ** 31 - 1, max(s_new, -2 ** 31))

    def remove(self, nums, key):
        """

        :param nums: list[int]
        :return: list[int],int
        """

        return nums, len(nums)

    def mysqrt(self, nums):
        """

        :param nums: int
        :return: int
        """
        # 牛顿法迭代，两个解无限接近
        if nums == 0:
            return 0
        x0, x1 = float('inf'), nums / 2
        while abs(x0 - x1) > 1e-6:
            x0 = x1
            x1 = (x0 + nums / x0) / 2
        return int(x0)


if __name__ == "__main__":
    so = Solution()
    # print(so.remove([1,2,3,2,2,5,4],2))
    print(so.mysqrt(8))
