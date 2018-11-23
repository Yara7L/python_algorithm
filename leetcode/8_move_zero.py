# 题目
# 给定一个数组 nums, 编写一个函数将所有 0 移动到它的末尾，同时保持非零元素的相对顺序。

# 例如， 定义 nums = [0, 1, 0, 3, 12]，调用函数之后， nums 应为 [1, 3, 12, 0, 0]。

# 注意事项:
# 必须在原数组上操作，不要为一个新数组分配额外空间。
# 尽量减少操作总数。

class Solution:
    def move_zero(self,nums):
        """
        :type nums:list[int]
        :rtype: list[int]
        """
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums.remove(0)
                nums.append(0)
                count+=1
        print(nums)
        return nums

    def move_zero_2(self,nums):
        """
        :type nums:list[int]
        :rtype: list[int]
        """
        count,i=0,0
        while i<len(nums):
            if nums[i]==0:
                nums.remove(0)
                count+=1
            else:
                i+=1
        nums.extend([0]*count)
        print(nums)
        return nums
    
    # 不断交换,最早出现的0 和 最迟出现的非零数
    # j的作用是按顺序记录0的位置
    def move_zero_3(self,nums):
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j],nums[i]=nums[i],nums[j]
            j+=1
        print(nums)
        return nums

if __name__=="__main__":
    test=Solution()
    nums=[2,0,1,3,0,2]
    test.move_zero(nums)
    test.move_zero_2(nums)
    test.move_zero_3(nums)
