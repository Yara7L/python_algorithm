# 统计所有小于非负数整数 n 的质数的数量。
#
# 示例:
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

class Solution(object):
    def countPrimes(self, num):
        """
        :param num:int
        :return: int,list[int]
        """
        res = []
        k = 0
        if num == 1:
            return 0
        for i in range(2, num + 1):
            count = 0
            # for j in range(1,i):
            # for j in range(1, i // 2 + 1):
            for j in range(1, int(i ** 0.5) + 1):
                if i % j == 0:
                    count += 1
            if count == 1:
                k += 1
                res.append(i)
        return k, res

    # 厄拉多塞筛法(Sieve of Eeatosthese)
    def countPrimes2(self, num):
        """
        :param num:int
        :return: int ,list[int]
        """
        num=num+1
        if num < 3:
            return 1
        res = [True] * num
        res[0] = res[1] = False
        for i in range(2, int(num ** 0.5) + 1):
            if res[i]:
                res[i * i:num:i] = [False] * len(res[i * i:num:i])
        return sum(res) , res


if __name__ == "__main__":
    test = Solution()
    print(test.countPrimes(17))
    print(test.countPrimes2(17))
