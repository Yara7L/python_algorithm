# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
#
# 你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#
# 返回获得利润的最大值。
#
# 示例 1:
#
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 注意:
#
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :param prices: list[int]
        :param fee: int
        :return: int
        """
        if max(prices) - min(prices) <= fee:
            return 0
        res = 0
        k = 0
        while k < len(prices) - 1:
            for j in range(k + 1, len(prices)):
                if prices[j] - prices[k] <= fee:
                    res = max(res, max(prices[0:j]) - min(prices[0:j]) - fee)
                    continue
                if prices[j] - prices[k] >= fee and prices[k] == min(prices[k:j]):
                    if j + 1 <= len(prices) - 1 and prices[j + 1] > prices[j]:
                        j = j + 1
                    res += prices[j] - prices[k] - fee
                break
            k = j + 1
        import numpy as np
        if max(np.where(max(prices))) < prices.index(min(prices)):
            res = 0
        print(np.where(max(prices) in prices))
        print(max(np.where(max(prices))))
        return res

    def maxprofit2(self, prices, fee):

        cash = 0  #该天结束的时候，手里没有彩票的情况下，已经获得的最大收益。
        hold = -prices[0]  #该天结束的时候，手里有彩票的情况下，已经获得的最大收益
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee) #可能今天买了，可能今天没买
            hold = max(hold, cash - prices[i])  #可能今天卖了，可能没卖
        return cash


if __name__ == "__main__":
    test = Solution()
    # prices = [1, 3, 3, 3, 2, 2, 2, 8, 4, 9]
    prices = [1, 3, 2, 8, 4, 9]
    # prices = [4, 5, 2, 4, 3, 3, 1, 2, 5, 4]
    # prices = [9, 8, 7, 1, 2]
    fee = 2
    # prices = [1, 3, 2, 8, 4, 9]

    # prices=[1,4,6,2,8,3,10,14]
    # print(test.maxProfit(prices, fee))
    print(test.maxprofit2(prices, fee))
