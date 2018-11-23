# 给定一个链表，判断链表中是否有环。
#
# 进阶：
# 你能否不使用额外空间解决此题？
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self,head):
        """
        :param head: ListNode
        :return: bool
        """
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                print("True")
                return True
            # return False
            else:
                print("False")
                return False

    def hasCycle_2(self,head):
        """
        :param head: ListNode
        :return: bool
        """
        cur=head.next
        while cur:
            if cur==head:
                return True
            else:
                return False
            cur=cur.next

if __name__=="__main__":
    test=Solution()
    

