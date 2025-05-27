class Solution:
    def leafNodes(self, preorder):
        stack = []
        leaf_nodes = []

        for i in range(len(preorder) - 1):
            current = preorder[i]
            next_val = preorder[i + 1]

            if next_val > current:
                count = 0
                while stack and next_val > stack[-1]:
                    last = stack.pop()
                    count += 1
                if count > 0:
                    leaf_nodes.append(current)
            else:
                stack.append(current)

        leaf_nodes.append(preorder[-1])

        return leaf_nodes