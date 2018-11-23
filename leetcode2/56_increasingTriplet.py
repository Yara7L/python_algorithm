# 给定一个未排序的数组，请判断这个数组中是否存在长度为3的递增的子序列。
#
# 正式的数学表达如下:
# 如果存在这样的i, j, k, 且满足0 ≤ i < j < k ≤ n - 1，
# 使得arr[i] < arr[j] < arr[k] ，返回true;否则返回false 。
# 要求算法时间复杂度为O(n)，空间复杂度为O(1) 。
#
# 示例:
# 输入[1, 2, 3, 4, 5],
# 输出true.
#
# 输入[5, 4, 3, 2, 1],
# 输出false.

# res[0]为递增序列的最小起点，res[1]为邻近res[0]的最小的
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :param nums: list[int]
        :return: bool
        """

        res = [float('inf'), float('inf')]
        for n in nums:
            if n > res[1]:
                return True
            if n <= res[0]:
                res[0] = n  #序列中最小的
            else:
                res[1] = n  #最小后面中，邻近res[0]的最小的
        return False


if __name__ == "__main__":
    test = Solution()
    nums = [8, 2, 6, 7, 5]
    print(test.increasingTriplet(nums))
