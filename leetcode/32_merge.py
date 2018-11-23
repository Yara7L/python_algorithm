# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]

class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :param nums1: list[int]
        :param m: int
        :param nums2: list[int]
        :param n: int
        :return: nums
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m- 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)
        return nums1

if __name__=="__main__":
    test = Solution()
    nums1 = [1, 2, 3, 4]
    m = len(nums1)
    nums2 = [1, 2, 6]
    n = len(nums2)
    # nums1+=nums2
    # print(nums1)
    for i in range(n):
        nums1.append(0)
    test.merge(nums1, m, nums2, n)
