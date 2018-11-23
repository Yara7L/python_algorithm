# 请编写一个函数，其功能是将输入的字符串反转过来。

# 示例：
# 输入：s = "hello"
# 返回："olleh"

class Solution:
    # python的切片
    def reverse_string(self,s):
        """
        :type s:str
        :rtype:str
        """
        r_str=s[::-1]
        print(r_str)

        l=list(s)
        l.reverse()
        r_s=''.join(l)
        print(r_s)

        return r_str
    

if __name__=="__main__":
    test=Solution()
    s="hello"
    test.reverse_string(s)