# 给出一个包含0, 1, 2, ..., n中n个数的序列，
# 找出0..n中没有出现在序列中的那个数。
#
# 案例1
# 输入: [3, 0, 1]
# 输出: 2
#
# 案例2
# 输入: [9, 6, 4, 2, 3, 5, 7, 0, 1]
# 输出: 8
#
# 注意事项:
# 您的算法应该以线性复杂度运行。你能否仅使用恒定的额外空间复杂度来实现它？

class Solution(object):
    def missingnumber(self, nums):
        """
        :param nums: list[int]
        :return: int
        """
        for i in range(0, len(nums)):
            if i not in nums:
                return i

    def missingnumber2(self,nums):
        """
        :param nums: list[int]
        :return: int
        """
        return (int(len(nums)*(len(nums)+1)/2)-sum(nums))

    def missingnumber3(self,nums):
        """
        :param nums: list[int]
        :return: int
        """
        return list(set(range(len(nums)+1))-set(nums))[0]


if __name__ == "__main__":
    test = Solution()
    print(test.missingnumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(test.missingnumber2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(test.missingnumber3([9, 6, 4, 2, 3, 5, 7, 0, 1]))