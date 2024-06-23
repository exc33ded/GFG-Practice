#User function Template for python3
class Solution:
	def bracketNumbers(self, str):
		# code here
		lst = []
        op = []
        count = 0
        for i in range(len(str)):
            if str[i]=="(":
                count += 1
                lst.append(count)
                op.append(count)
            elif str[i]==")":
                p = lst.pop()
                op.append(p)
        return op




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        answer = ob.bracketNumbers(S)
        for value in answer:
            print(value, end=" ")
        print()

# } Driver Code Ends