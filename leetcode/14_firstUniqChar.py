# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

# 案例:

# s = "leetcode"
# 返回 0.

# s = "loveleetcode",
# 返回 2.
 
# 注意事项：您可以假定该字符串只包含小写字母。

class Solution:
    def first_uniqchar(self,s):
        """
        :type s: str
        :rtype:int
        """
        lowercase='abcdefghijklmnopqrstuvwxyz'
        res=[s.index(letter) for letter in lowercase if s.count(letter)==1]
        if len(res):
            print(min(res))
            return min(res)
        return -1
    
    # 用字典记录各字符的索引。如果重复出现，则索引值需要加上len(s)
    def first_uniqchar_2(self,s):
        """
        :type s: str
        :rtype:int
        """
        d={}
        for i in range(len(s)):
            if s[i] not in d :
                d[s[i]]=i
            else:
                d[s[i]]+=len(s)
        if len(s) and min(d.values())<len(s):
            print(min(d.values()))
            return min(d.values())
        else:
            return -1

if __name__=="__main__":
    test=Solution()
    s="leetcode"
    test.first_uniqchar(s)
    test.first_uniqchar_2(s)

