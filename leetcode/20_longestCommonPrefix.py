# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:
# 输入: ["flower","flow","flight"]
# 输出: "fl"

# 示例 2:
# 输入: ["dog","racecar","car"]
# 输出: ""

# 解释: 输入不存在公共前缀。
# 说明:所有输入只包含小写字母 a-z 。

class Solution:
    def longestCommonProfix(self,ls):
        """
        :type ls:list[str]
        :rtpye:str
        """
        shortest = min(ls, key=len)
        for i, ch in enumerate(shortest):
            for s in ls:
                if s[i] != ch:
                    
                    return shortest[: i]
        print(shortest)
        return shortest

    def longestCommonProfix_2(self,ls):
        string = ''
        if strs:
            for i in range(len(strs[0])):
                old_str = string
                string += strs[0][i]
                for j in range(1, len(strs)):
                    if strs[j][: i + 1] != string:
                        return old_str
        return string

if __name__=="__main__":
    test=Solution()
    ls=["flower","flow","flight"]
    test.longestCommonProfix(ls)
