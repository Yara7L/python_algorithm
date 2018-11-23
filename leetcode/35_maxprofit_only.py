# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

# 示例 2:
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

class Solution:
    #动态规划，找最小的买，找最大的卖
    def max_profit(self,nums):
        """
        :param nums: list[int]
        :return: int
        """
        if len(nums) < 2:
            return 0
        minP = nums[0]
        profit = 0
        for p in nums:
            profit = max(profit, p - minP)
            minP = min(minP, p)
        return profit

    # 遍历找出数组，找出差值最大，O(n**2)
    def max_profit_2(self,nums):
        """
        :param nums:list[int]
        :return: int
        """
        maxprofit=0
        for i in range(len(nums)-1):
            fit=max(nums[i+1:])-nums[i]
            if fit>maxprofit:
                maxprofit=fit
        return  maxprofit

if __name__=="__main__":
    test=Solution()
    nums=[2,5,7,1,4,0]
    print(test.max_profit(nums))
    print(test.max_profit_2(nums))