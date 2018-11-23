# 给定一个字符串，找出不含有重复字符的最长子串的长度。
#
# 示例：
# 给定"abcabcbb" ，没有重复字符的最长子串是"abc" ，那么长度就是3。
#
# 给定 "bbbbb" ，最长的子串就是"b" ，长度是1。
#
# 给定"pwwkew" ，最长子串是"wke" ，长度是3。
#
# 请注意答案必须是一个子串，"pwke"是子序列而不是子串。

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :param s: str
        :return: int
        """
        res = ''
        maxlen = 0
        for ch in s:
            if ch not in res:
                res += ch
            else:
                maxlen = max(maxlen, len(res))
                index = res.index(ch)  #找到与当前字符重复的位置，重新开始字串
                res = res[index + 1:] + ch  #新的字串
        return max(maxlen, len(res))


if __name__ == "__main__":
    test = Solution()
    s = "abcabcbb"
    print(test.lengthOfLongestSubstring(s))
