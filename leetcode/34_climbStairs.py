# 假设你正在爬楼梯。需要 n 步你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 步 + 1 步
# 2.  2 步

# 示例 2：
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 步 + 1 步 + 1 步
# 2.  1 步 + 2 步
# 3.  2 步 + 1 步

# 每一步都是 前两步和前一步 的和
class Solution:
    def climbStairs(self, num):
        """
        :param num:int
        :return: int
        """
        if num == 1:
            res = 1
        elif num == 2:
            res = 2
        else:
            res = self.climbStairs(num - 1) + self.climbStairs(num - 2)
        # print(res)
        return res

    def climbStairs_2(self, num):
        """
        :param num:int
        :return: int
        """
        pre, cur = 1, 1
        for i in range(1, num):
            pre, cur = cur, pre + cur
        return cur

    def climbStair_3(self,num):
        """
        :param num:int
        :return: int
        """
        if num == 1:
            return 1
        elif num == 2:
            return 2
        res=[1,2]
        for i in range(2,num):
            res.append(res[i-1]+res[i-2])
        return res[-1]


if __name__ == "__main__":
    test = Solution()
    test.climbStairs(10)
    print(test.climbStairs(10))
    print(test.climbStairs_2(10))
    print(test.climbStair_3(10))
