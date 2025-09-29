class Solution:
    def binstr(self, n):
        return [bin(i)[2:].zfill(n) for i in range(0, (2 ** n))]
        