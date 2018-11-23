# 反转链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, pre = head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def reverseList_2(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.reverseList_2(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return newHead


if __name__ == "__main__":
    test = Solution()
    test.reverseList()
