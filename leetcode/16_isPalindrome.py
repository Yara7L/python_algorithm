# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:
# 输入: "A man, a plan, a canal: Panama"
# 输出: true

# 示例 2:
# 输入: "race a car"
# 输出: false
import re
from string import punctuation


class Solution:
    def isPalindrome(self, s):
        """
        :type s:str
        :rtype: bool
        """
        # 处理字符串，去掉符号，大写变为小写
        # s=[i for i in s.lower()]
        # print(s)
        # res=s==s[::-1]
        # print(res)
        # return res

        s_new = [char for char in s.lower() if char.isalnum()]
        print(s_new)
        res = s_new == s_new[::-1]
        print(res)
        return res

    def isPalindrome_2(self, s):
        """
        :type s:str
        :rtype: bool
        """
        s_new = list(filter(str.isalnum, s.lower()))
        print(s_new)
        res = s_new == s_new[::-1]
        print(res)
        return res


if __name__ == "__main__":
    test = Solution()
    s = "A man, a plan, a canal: Panama"
    test.isPalindrome(s)
    test.isPalindrome_2(s)
