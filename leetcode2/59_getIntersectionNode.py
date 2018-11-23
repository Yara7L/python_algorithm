# 编写一个程序，找到两个单链表相交的起始节点。
#
# 例如，下面的两个链表：
#
#       A: a1 → a2
#                   ↘
#                     c1 → c2 → c3
#                   ↗
# B: b1 → b2 → b3
# 在节点c1开始相交。
#
# 注意：
# 如果两个链表没有交点，返回null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足O(n)时间复杂度，且仅用O(1)内存。

class ListNode(object):
    def __init__(self, num):
        self.value = num
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :param headA: ListNode
        :param headB: ListNode
        :return: ListNode
        """
        if headA == None or headB == None:
            return
        a, b = headA, headB
        la, lb = 1, 1  # A，B的长度
        while a.next:
            la += 1
            a = a.next
        while b.next:
            lb += 1
            b = b.next
        if a.value != b.value:
            return

        a, b = headA, headB  # 回到头节点
        if lb > la:
            # 如果B比A长，A右移动
            for _ in range(lb - la):
                b = b.next
        else:
            for _ in range(la - lb):
                a = a.next
        while a:  # 重新遍历，一定能发现重复的点,重复一个点也交做相交了
            if a.value == b.value:
                return a
            a = a.next
            b = b.next


if __name__ == "__main__":
    test = Solution()
    headA = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    headA.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    headB = ListNode(1)
    ll1 = ListNode(1)
    ll2 = ListNode(1)
    ll3 = ListNode(3)
    ll4 = ListNode(4)
    ll5 = ListNode(5)
    headB.next = ll1
    ll1.next = ll2
    ll2.next = ll3
    ll3.next = ll4
    ll4.next = ll5
    print(test.getIntersectionNode(headA, headB))
