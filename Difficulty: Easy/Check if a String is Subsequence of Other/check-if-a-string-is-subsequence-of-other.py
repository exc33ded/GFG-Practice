class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        s1_pt = 0
        s2_pt = 0
        
        while s1_pt < len(s1) and s2_pt < len(s2):
            if s1[s1_pt] == s2[s2_pt]:
                s1_pt += 1
            s2_pt += 1
            
        if s1_pt == len(s1):
            return True
        else:
            return False
        