# 给定一个 32 位有符号整数，将整数中的数字进行反转。

# 示例 1:
# 输入: 123
# 输出: 321

#  示例 2:
# 输入: -123
# 输出: -321

# 示例 3:
# 输入: 120
# 输出: 21

# 注意:
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
# 根据这个假设，如果反转后的整数溢出，则返回 0。

class Solution:
    # 正数可行，负数不可行
    def reserve_int(self,num):
        """
        :type num: int
        :rtype:int
        """
        flag=True
        if num<0:
            num=num*(-1)
            flag=False

        res=0
        while num!=0:
            k=num%10
            tmp=res
            res=tmp*10+k
            num=num//10            
            if res//10 != tmp:
                print("溢出")
                return 0
        if flag==False:
            print(res*(-1))
            return res*(-1)
        else:
            print(res)
            return res
    
    # 不太明白
    def reserve_int_2(self,num):
        """
        :type num: int
        :rtype:int
        """
        # 匿名函数确定num的正负性
        s = lambda num: num and [1, -1][num < 0]
        r = int(str(s(num) * num )[: : -1])
        print(s(num) * r * (r < 2**31 - 1))
        return s(num) * r * (r < 2**31 - 1)

    def reserve_int_3(self,num):
        """
        :type num: int
        :rtype:int
        """
        result=int(str(abs(num))[::-1])
        if num>0 and result < 2**31:
            print(result)
            return result
        if num<0:
            result=-result
            if result>-2**31:
                print(result)
                return result


if __name__=="__main__":
    test=Solution()
    num=122
    # test.reserve_int(num)
    test.reserve_int_2(num)
    # test.reserve_int_3(num)