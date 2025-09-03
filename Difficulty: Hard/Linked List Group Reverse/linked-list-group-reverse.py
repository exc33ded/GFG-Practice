"""
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""

class Solution:
    def reverseKGroup(self, head, k):
        arr = []
        _head = head
        _init_head = head
        counter = 0 
        while _head:
            arr.append(_head.data)
            counter += 1
            _head = _head.next
            if counter == k:
                while arr:
                    _init_head.data = arr.pop()
                    _init_head = _init_head.next
                counter = 0
        while arr:
            _init_head.data = arr.pop()
            _init_head = _init_head.next
        return head