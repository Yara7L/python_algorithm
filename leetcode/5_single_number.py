# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

# 示例 1:
# 输入: [2,2,1]
# 输出: 1

# 示例 2:
# 输入: [4,1,2,1,2]
# 输出: 4

# 将整个数组进行相与（异或）位运算，最后的结果即为目标数。相同为0，不同为1
class Solution:
    def single_number(self,arr):
        """
        :type arr:list[int]
        :rtype : int
        """
        length=len(arr)
        ret,i = 0,0
        while i<length:
            ret=ret^arr[i]
            i+=1
        print(ret)
        return ret
    
    def select_sort(self,lists):
        # '''选择排序'''
        count=len(lists)
        for i in range(0,count):
            min=i
            for j in range(i+1,count):
                if lists[min]>lists[j]:
                    min=j
            lists[min],lists[i]=lists[i],lists[min]
        print(lists)
        return lists

    def single_number_sort(self,arr):
        """
        :type arr:list[int]
        :rtype : int
        """
        nums=self.select_sort(arr)
        for i in range(len(nums)):
            if len(nums) == 1:
                print(nums)
                return nums[0]
            if nums[0] == nums[1]:
                del nums[0]
                del nums[0]
            else:
                print(nums)
                return nums[0]

# 其他元素都出现了三次，按位计算每一位上1的个数，结果模3为1的那些位就是所求数二进制1所在的位。
    def single_number_three(self,arr):
        """
        :type arr:list[int]
        :rtype : int
        """
        ret =0

# 给一个数组，其中里面有两个数只出现一次，其他的均出现两次。找出这两个数。
    def two_numbers_single(self,arr):
        """
        :type arr:list[int]
        :rtype : int
        """
        length=len(arr)
        two,i = 0,0
        while i<length:
            two=two^arr[i]
            i+=1
        print(two)

        # 得出两个数异或结果的最右边的一个1，其他的为零
        # 这样进行&操作就可以将两个不同的数分到不同的两组去
        two &=-two
        i=0
        a,b=0,0
        while i<length:
            if two&arr[i]==0:
                a ^= arr[i]
            else:
                b ^=arr[i]
            i+=1
        print(a,b)
        return a,b




if __name__=="__main__":
    test=Solution()
    arr=[1,2,1,3,2,4,3]
    test.single_number(arr)
    # test.select_sort(arr)
    test.single_number_sort(arr)

    arr=[1,2,1,3,2,4]
    test.two_numbers_single(arr)