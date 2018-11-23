# 给定两个数组，写一个方法来计算它们的交集。

# 例如:
# 给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].

# 注意：
#    输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
#    我们可以不考虑输出结果的顺序。

# 跟进:
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？

class Solution:
    def intersect(self,nums1,nums2):
        """
        :param nums1: list[int]
        :param nums2: list[int]
        :return: list[int]
        """
        print(list(set(nums1).intersection(set(nums2))))
        print(list(set(nums1).union(set(nums2))))
        print(list(set(nums1).difference(set(nums2))))

        # import collections
        # a, b = map(collections.Counter, (nums1, nums2))
        # return list((a & b).elements()

        res = []
        for k in nums1:
            if k in nums2:
                res.append(k)
                nums2.remove(k)
        print(res)
        return res

if __name__=="__main__":
    test=Solution()
    a=[1,2,3,5,4]
    b=[2,3,6,7]
    test.intersect(a,b)
