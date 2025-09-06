'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        if head is None or head.next is None:
            return 0;
            
        slow=head
        fast = head
        c=1
        
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast: break
        if fast is None or fast.next is None:
            return 0
        slow=fast.next
        while slow is not fast:
            c+=1
            slow=slow.next
        return c  
        