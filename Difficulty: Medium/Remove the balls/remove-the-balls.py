#User function Template for python3
class Solution:
    def findLength(self, color, radius):
        stack = []
        for c, r in zip(color, radius):
            if stack and stack[-1] == (c, r):
                stack.pop()
                continue
            stack.append((c, r))
        return len(stack)