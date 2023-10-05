#User function Template for python3

def searchPattern(st, pat):
    # code here
    return True if pat in st else False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(t):
    st=input()
    pat=input()
    if (searchPattern(st, pat)):
        print("Present")
    else:
        print("Not present")
# } Driver Code Ends