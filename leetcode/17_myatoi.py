# 实现 atoi，将字符串转为整数。

# 在找到第一个非空字符之前，需要移除掉字符串中的空格字符。
# 如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。
# 如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

# 当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

# 若函数不能执行有效的转换，返回 0。

# 说明：
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。
# 如果数值超过可表示的范围，则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

# 示例 1:
# 输入: "42"
# 输出: 42

# 示例 2:
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

# 示例 3:
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

# 示例 4:
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。

# 示例 5:
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
#      因此返回 INT_MIN (−231) 。

import re 

class Solution:
    def mystoi(self,s):
        """
        :type s:str
        :rtype:int
        """
        int_=['0','1','2','3','4','5','6','7','8','9','-']
        res=''
        # res=[] res.append(s[])  res=int(''.join(res))
        i=0
        length=len(s)
        if s[0] in int_:
            res+=s[0]
            while i<length-1:
                i+=1
                if s[i] in int_:
                    res+=s[i]
                else:
                    break
            res=int(res)
            if res>2**31-1:
                res=2**31-1
            elif res<-2*31:
                res=-2**31
            else:
                res=res
            print(res)
            return res
        else:
            print('0')
            return 0
    
    # 正则表达式查找目标字符串
    def mystoi_1(self,s):
        """
        :type s:str
        :rtype:int
        """
        res = re.findall(r"^[\+\-]?\d+", s.strip())
        if res != []:
            if int(res[0]) > (2 ** 31 - 1):
                s_new=2 ** 31 - 1
            elif int(res[0]) < (-2 ** 31):
                s_new=-2 ** 31
            else:
                s_new=int(res[0])
        else:
            s_new=0
        print(s_new)
        return s_new
    
    def mystoi_2(self,s):
        """
        :type s:str
        :rtype:int
        """ 
        s_new = ''
        s = s.lstrip()
        if s.startswith('+') or s.startswith('-'):
            s_new += s[0]
            s = s[1:]
        
        for ch in s:
            if ch.isdigit():
                s_new += ch
            else:
                break
        
        if s_new.lstrip('+-').isdigit():
            s_new = int(s_new)
        else:
            return 0
        
        print(min(2**31 - 1, max(-2**31, s_new)))
        return min(2**31 - 1, max(-2**31, s_new))



if __name__=="__main__":
    test=Solution()
    # s="-9003jidj"
    s="-91283472332"
    test.mystoi(s)
    test.mystoi_1(s)
    test.mystoi_2(s)
