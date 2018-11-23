# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
#
# 示例:
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
#     ["ate", "eat", "tea"],
#     ["nat", "tan"],
#     ["bat"]
# ]
# 说明：
# 所有输入均为小写字母。
# 不考虑答案输出的顺序。
class Solution(object):
    def groupanagram(self, s):
        """
        :param s: list[str]
        :return:list[list[str]]
        """
        d = {}
        for ch in s:
            s_sorted = ''.join(sorted(ch))
            if s_sorted not in d:
                d[s_sorted] = [ch]
            else:
                d[s_sorted].append(ch)
        return [value for value in d.values()]


if __name__ == "__main__":
    test = Solution()
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(test.groupanagram(s))
