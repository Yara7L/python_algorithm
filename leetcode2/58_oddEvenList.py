# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
# 请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

class ListNode(object):
    def __init__(self, num):
        self.value = num
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        """

        :param head: ListNode
        :return: ListNode
        """
        if head == None or head.next == None or head.next.next == None:
            return head
        # 1 2 3 4 5 6，1 3 5 2 4 6
        even = head.next
        odd = head.next.next
        head.next = odd
        t = even
        while odd.next:
            even.next = even.next.next
            even = even.next
            odd.next = odd.next.next
            if even.next:
                odd = odd.next
        odd.next = t  # 连上第一个偶数位
        even.next = None  # 偶数位的最后连上None
        return head


if __name__ == "__main__":
    test = Solution()
    head = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    head.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l6
    print(test.oddEvenList(head))
