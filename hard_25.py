# -*- coding: utf-8 -*-
# Author: Weichen Liao
'''
25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # reverse linklist, return the head and the tail
        def reverseLinkList(head: ListNode):
            if head == None:
                return head, head
            listOfNodes = [head]
            while head.next:
                listOfNodes.append(head.next)
                head = head.next
            listOfNodes = listOfNodes[::-1]
            for i,item in enumerate(listOfNodes):
                if i != len(listOfNodes)-1:
                    listOfNodes[i].next = listOfNodes[i+1]
                else:
                    listOfNodes[i].next = None
            return listOfNodes[0], listOfNodes[-1]

        if head == None or head.next == None:
            return head
        count = 0
        while True:



node0 = ListNode(val=0)
node1 = ListNode(val=1)
node2 = ListNode(val=2)
node3 = ListNode(val=3)
node0.next = node1
node1.next = node2
node2.next = node3

s = Solution()
nodeHead = s.reverseKGroup(node0,1)

while nodeHead and nodeHead.next:
   print(nodeHead.val)
   nodeHead = nodeHead.next
print(nodeHead.val)