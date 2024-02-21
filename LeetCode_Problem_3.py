# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #建立鏈表
        head = ListNode()
        current = head
        carry = 0

        
        while(l1 != None or l2 != None or carry != 0 ):
            l1_value = 0 if l1 is None else l1.val
            l2_value = 0 if l2 is None else l2.val
            total = l1_value + l2_value + carry
            current.next = ListNode(total % 10)
            #處裡多的位數
            carry = total // 10
            l1= None if l1 is None else l1.next
            l2= None if l2 is None else l2.next
            current = current.next
        return head.next
        