# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.

# 说明：
# 给定的 n 保证是有效的。
#
# 进阶：
# 你能尝试使用一趟扫描实现吗？
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :param head: ListNode
        :param n: int
        :return: ListNode
        """
        if not head.next:
            return

        p = head
        count = 1
        while p.next:
            p = p.next
            count += 1

        pre, cur = head, head
        if count == n:
            pre.val = pre.next.val
            pre.next = pre.next.next
        for _ in range(count - n):
            pre = cur
            cur = cur.next
        pre.next = cur.next
        return head

if __name__=="__main__":
    test=Solution()
    head=1
    n=3
    test.removeNthFromEnd(head,n)