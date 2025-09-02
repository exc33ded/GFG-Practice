"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        #return head of reverse doubly linked list
        while head.next != None:
            head.prev,head.next,head=head.next,head.prev,head.next
        head.next,head.prev=head.prev,None
        return head    