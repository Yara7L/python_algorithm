# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

# 示例:
# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

class Solution:
    def twosum(self,nums,target):
        """
        :type nums:list[int]
        :type target:int
        :rtype:list[int]
        """
        for i in range(len(nums)):
            t=target-nums[i]
            if t in nums and nums.index(t)!=i:
                print([nums.index(t),i])
                return [nums.index(t),i]
    
    def twosum_2(self,nums,target):
        """
        :type nums:list[int]
        :type target:int
        :rtype:list[int]
        """
        # 创建字典，键值对：数字--索引;
        # 数字去查找索引
        d={}
        for i in range(len(nums)):
            t=target-nums[i]
            if t in d:
                print([d[t],i])
                return [d[t],i]
            d[nums[i]]=i

    
if __name__=="__main__":
    test=Solution()
    nums=[5,6,9,5]
    target=10
    test.twosum(nums,target)
    test.twosum_2(nums,target)