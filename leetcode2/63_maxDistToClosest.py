# 在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
# 至少有一个空座位，且至少有一人坐在座位上。
#
# 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
# 返回他到离他最近的人的最大距离。
#
# 示例 1：
# 输入：[1,0,0,0,1,0,1]
# 输出：2
# 解释：
# 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
# 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
# 因此，他到离他最近的人的最大距离是 2 。
#
# 示例 2：
# 输入：[1,0,0,0]
# 输出：3
# 解释：
# 如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
# 这是可能的最大距离，所以答案是 3 。
# 提示：
# 1 <= seats.length <= 20000
# seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :param seats: list[int]
        :return: int
        """
        #         连续0最多的
        length = len(seats)
        zeros = []
        zeros_count = 0
        for i in range(length):
            if seats[i] == 0:
                zeros_count += 1
            if seats[i] == 1:
                zeros_count = 0
            zeros.append(zeros_count)
        zeros_count = max(zeros)
        print(zeros)
        print(len(zeros))

        zero_index = zeros.index(zeros_count)

        if zeros_count == 1:  # 只存在1
            return 1
        if zeros_count == zero_index + 1:  # 在首位，0最多
            return zeros_count
        if zeros_count == zeros[length - 1] or zeros_count - 1 == zeros[length - 1]:  # 0最多在末尾 或 0次多在末尾
            return zeros[length - 1]
        if zeros.index(zeros_count - 1) + 1 == zeros_count - 1:  # 在首位，0次多
            return zeros_count - 1
        else:  # 中间情况
            return zeros_count // 2 if zeros_count % 2 == 0 else zeros_count // 2 + 1


if __name__ == "__main__":
    test = Solution()
    seats = [1, 0, 0, 0, 1, 1, 1]
    # seats = [1, 0, 0, 0]
    # seats = [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0]
    # seats=[1, 1, 0, 1, 1]
    # seats = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1]
    # seats=[0,1]
    # seats=[0,0,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0]
    seats = [0, 1, 1, 1, 0, 0, 1, 0, 0]
    print(test.maxDistToClosest(seats))
