# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
# 输入: "()"
# 输出: true
#
# 示例 2:
# 输入: "()[]{}"
# 输出: true
#
# 示例 3:
# 输入: "(]"
# 输出: false
#
# 示例 4:
# 输入: "([)]"
# 输出: false
#
# 示例 5:
# 输入: "{[]}"
# 输出: true
class Solution(object):
    def isvalid(self, s):
        """
        :param s: str
        :return: bool
        """
        x = ['(', '{', '[']
        y = [')', '}', ']']
        z = ['()', '{}', '[]']
        res = []
        for i in s:
            if i in x:
                # 左括号入栈
                res.append(i)
            elif i in y:
                # 如果是右括号，对比栈中是否有左括号
                if res == []:
                    # 若为空，则返回false
                    return False
                else:
                    # 与栈顶左括号匹配，是否为一对
                    temp = res.pop(-1) + i
                    if temp not in z:
                        return False
        # 若右括号与左括号都匹配，栈中是否有左括号
        if len(res) != 0:
            return False
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.isvalid('(({}))[]'))
