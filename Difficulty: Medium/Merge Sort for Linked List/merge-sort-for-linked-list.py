'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergeSort(self, head):
        # Base case: if the list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head

        # Find the middle of the list
        middle = self.getMiddle(head)
        next_of_middle = middle.next
        middle.next = None  # Split the list into two halves

        # Recursively sort the two halves
        left = self.mergeSort(head)
        right = self.mergeSort(next_of_middle)

        # Merge the sorted halves
        sorted_list = self.sortedMerge(left, right)
        return sorted_list

    def getMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head.next  # Start fast one step ahead for even length lists

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, a, b):
        result = None

        # Base cases
        if not a:
            return b
        if not b:
            return a

        # Pick either a or b, and recur
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
        