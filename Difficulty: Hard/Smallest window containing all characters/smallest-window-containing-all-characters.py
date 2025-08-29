class Solution:
     def smallestWindow(self, s, p):
        # code here
        # algorithm, make a counter variable to count the how many letters that have covered
        # string p
        # only when counter_of_s[e] <= counter_of_p[e], that letter e will contribute to the counter
        # if counter_of_s[e] > counter_of_p[e] then letter e is redundant. does not contribute toe the counter
        
        from collections import Counter
        
        pct = Counter(p)
        counter = 0   #when any letter in p has been covered, then counter increase by 1
        
        left = 0
        ans = None
        sct = Counter()
        
        for r, e in enumerate(s):
            if e not in p: # skip not in p
                continue
            
            sct[e] += 1
            if sct[e] <= pct[e]:  #if sct[e] > pct[e] then e dosn't contribute the coverage of p
                counter += 1
            
            # now we are in the window that covers all the letters in p    
            while left <= r and counter >= len(p):
                if ans is None or len(ans) > r-left+1:
                    ans = s[left:r+1]
                leftc = s[left]
                if leftc in sct:
                    sct[leftc] -= 1
                    if sct[leftc] < pct[leftc]:
                        counter -= 1
                left += 1
            
        return "" if not ans else ans