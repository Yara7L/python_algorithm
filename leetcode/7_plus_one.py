# 给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例 1:
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。

# 示例 2:
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
import numpy as np
class Solution:
    def plus_one(slef,nums):
        """
        :type nums:list[int]
        :rtype : list[int]
        """
        length=len(nums)
        if nums[0]==0 and length>1:
            print("除整数0以外，首位不能为0，请重新输入")
            nums=input('input nums:') 
            # #输入有问题

        # import getpass
        # password=getpass.getpass('请输入密码：')
        # 需要多次进位操作的时候呢，最后的位数变化了呢
        
    # list==>int ==> plus_one ==>str
        num = 0
        for i in nums:
            num = 10 * num + i
        nums_plus=[int(x) for x in str(num+1)]
        print(nums_plus)

        # list==>str  str==>int plus_one int==>str
        # plus=''
        # i=0
        # while i<length:
        #     plus+=str(nums[i])
        #     i+=1
        # plus=int(plus)
        # plus=plus+1
        # nums=str(plus)
        # nums_plus=[int(x) for x in nums]
        # print(nums_plus)
    # 列表解析和join的函数式求int
        nums = [str(i) for i in nums]
        num = int(''.join(nums))
        # S.join(iterable),把字符串用指定的符号链接起来，返回字符串格式
        
        nums_plus=[int(x) for x in str(num + 1)]
        print(nums_plus)

        # digits[0] += 1;
        # for(int i = 0;i < len;++i){
        #    cur = (digits[i]+carry)%10;
        #    carry = (digits[i]+carry)/10;
        #    digits[i] = cur;
        # }
        # 记住最后的进位即可

        return nums_plus

if __name__=="__main__":
    test=Solution()
    nums=[3,0,1]
    test.plus_one(nums)
        
        


