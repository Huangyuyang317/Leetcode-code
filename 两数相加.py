class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if  not l2:
            return l1
        if not l1:
            return l2
        else:
            l1.val +=l2.val
            if l1.val>= 10:
                l1.val=l1.val%10
                l1.next=self.addTwoNumbers(ListNode(1),l1.next)
                # l1.next.val=1 是错误的，因为只加1的话 99999和999相加，就会出现10而不是迭代
            l1.next=self.addTwoNumbers(l1.next,l2.next)
        return l1