# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self,L1,L2):
        """
        :param L1:ListNode
        :param L2: ListNode
        :return: ListNode
        """
        if not L1 and not L2:
            return

        res=[]
        q1,q2=L1.L2
        while q1:
            res.append(q1)
            q1=q1.next
        while q2:
            res.append(q2)
            q2=q2.next
        res=sorted(res,key=lambda x:x.val)
        print([i.val for i in res])
        return [i.val for i in res]

if __name__=="__main__":
    test=Solution()
