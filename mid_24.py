# -*- coding: utf-8 -*-
# Author: Weichen Liao
'''
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

'''
用递归函数，每每交换前两个node，后面的node用递归迭代
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        elif head.next != None:
            if head.next.next != None:
                nodeNext = head.next
                head.next = self.swapPairs(head=head.next.next)
                nodeNext.next = head
                return nodeNext
            else:
                nodeNext = head.next
                nodeNext.next = ListNode(val=head.val)
                return nodeNext

        else:
            return head




node0 = ListNode(val=0)
node1 = ListNode(val=1)
node2 = ListNode(val=2)
node3 = ListNode(val=3)
node0.next = node1
node1.next = node2
node2.next = node3

s = Solution()
nodeHead = s.swapPairs(head=node0)
print(nodeHead.val)
print(nodeHead.next.val)
print(nodeHead.next.next.val)
print(nodeHead.next.next.next.val)


