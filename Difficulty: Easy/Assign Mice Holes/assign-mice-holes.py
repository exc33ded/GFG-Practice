class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices.sort()
        holes.sort()
        final = 0
        
        for i in range(len(mices)):
            final = max(final, abs(mices[i] - holes[i]))
    
        return final