def transitionPoint(arr, n):
    #Code here
    lb = 0
    ub = n - 1
  
    while (lb <= ub):
        mid = (int)((lb + ub) / 2)

        if (arr[mid] == 0):
            lb = mid + 1
        elif (arr[mid] == 1):

            if (mid == 0 \
                or (mid > 0 and\
                arr[mid - 1] == 0)):
                return mid
  
            ub = mid-1
      
    return -1
    
#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))

# } Driver Code Ends