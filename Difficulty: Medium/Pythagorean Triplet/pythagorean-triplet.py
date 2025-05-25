class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	squared = [x * x for x in arr]
        n = len(squared)
        squared_set = set(squared)

        for i in range(n):
            for j in range(i + 1, n):
                if squared[i] + squared[j] in squared_set:
                    return True
        return False