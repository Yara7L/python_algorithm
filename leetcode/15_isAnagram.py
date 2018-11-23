# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

# 例如，
# s = "anagram"，t = "nagaram"，返回 true
# s = "rat"，t = "car"，返回 false

# 注意:
# 假定字符串只包含小写字母。

# 提升难度:
# 输入的字符串包含 unicode 字符怎么办？你能能否调整你的解法来适应这种情况？

# 统计出现的字符以及对应的数量
class Solution:
    def isAnagram(self,s,t):
        """
        :type s:str
        :type t:str
        :rtype :bool
        """
        res=set(s)==set(t) and all((s.count(i)==t.count(i)) for i in set(s))
        print(res)
        return res

    def isAnagram_2(self,s,t):
        """
        :type s:str
        :type t:str
        :rtype :bool
        """
        from collections import Counter
        # print(Counter(s))
        res=Counter(s)==Counter(t)
        print(res)
        return res


if __name__=="__main__":
    test=Solution()
    s="aabbanagrkooklam"
    t="nagaraaabbmookkl"
    test.isAnagram(s,t) 
    test.isAnagram_2(s,t)   
