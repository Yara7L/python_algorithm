# 写一个程序，输出从 1 到 n 数字的字符串表示。
#
# 1. 如果 n 是3的倍数，输出“Fizz”；
# 2. 如果 n 是5的倍数，输出“Buzz”；
# 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

# 示例：
# n = 15,
# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

class Solution(object):
    def fizzbuzz(self, num):
        """
        :param num: int
        :return: list[str]
        """
        res = []
        for i in range(0, num):
            if (i + 1) % 3 == 0 and (i + 1) % 5 == 0:
                res.append('fizzbuzz')
            elif (i + 1) % 3 == 0:
                res.append('fizz')
            elif (i + 1) % 5 == 0:
                res.append('buzz')
            else:
                res.append(str(i + 1))
        return res


if __name__ == "__main__":
    test = Solution()
    print(test.fizzbuzz(15))
    print(3%3)
