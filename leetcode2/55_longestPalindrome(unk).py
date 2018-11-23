# 给定一个字符串s，找到s中最长的回文子串。你可以假设s的最大长度为1000。
#
# 示例1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
#
# 示例2：
# 输入: "cbbd"
# 输出: "bb"

# 对比第
class Solution(object):
    def longestPalindrome(self, s):
        """

        :param s: str
        :return: str
        """
        n = len(s)
        maxl = 0  #记录字串长度
        start = 0
        for i in range(n):
            # 比较范围更大，增加比较字串的前一位，匹配当前新增的字符，判断是否是回文
            if i - maxl >= 1 and s[i - maxl - 1:i + 1] == s[i - maxl - 1:i + 1][::-1]:
                start = i - maxl - 1
                maxl += 2
                continue
            #  比较临近的
            if i - maxl >= 0 and s[i - maxl:i + 1] == s[i - maxl:i + 1][::-1]:
                start = i - maxl
                maxl += 1
        return s[start:start + maxl]


if __name__ == "__main__":
    test = Solution()
    s = "cbbabbc"
    print(test.longestPalindrome(s))
