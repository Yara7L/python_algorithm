# 给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
#
# 你可以假设除了数字0之外，这两个数字都不会以零开头。
#
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

class ListNode(object):
    def __init__(self, num):
        self.value = num
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        l = ListNode(0)
        while l1:
            l.next = ListNode(0)
            if l1.value + l2.value >= 10:
                l.value = l1.value + l2.value - 10
                l.next.value = 1
            else:
                # 为什么不能上一个节点的next，不等于，当前节点呢
                l.value = l.value + l1.value + l2.value
            print('l.value:{0}'.format(l.value))
            l1 = l1.next
            l2 = l2.next
        return l

    def addTwoNumbers2(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        i, s1, l = 1, 0, l1
        while l:
            s1 += l.value * i
            i = i * 10
            l = l.next
        i, s2, l = 1, 0, l2
        while l:
            s2 += l.value * i
            i *= 10
            l = l.next
        s = s1 + s2
        s = str(s)[::-1]
        res = [ListNode(int(ch)) for ch in s]
        for i in range(len(res) - 1):
            res[i].next = res[i + 1]
        return res[0]


if __name__ == "__main__":
    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3
    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6
    test = Solution()
    print(test.addTwoNumbers(l1, l4))
    print(test.addTwoNumbers2(l1, l4))
