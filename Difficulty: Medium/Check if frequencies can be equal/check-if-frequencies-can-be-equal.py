from collections import Counter
class Solution:
    def sameFreq(self, s: str) -> bool:
        ctr=Counter(s)
        if len(set(ctr.values()))==1:
            return True
        for key in ctr.keys():
            ctr[key]-=1
            st=set(ctr.values())
            st.discard(0)
            if len(st)==1:
                return True
            ctr[key]+=1
        return False