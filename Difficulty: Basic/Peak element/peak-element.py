
class Solution:   
    def peakElement(self,arr):
        # Code here
        n = len(arr)
        
        start = 0
        end = n - 1
        
        while (start < end):
            mid = start + (end - start)//2
            
            if arr[mid] > arr[mid + 1]:
                if arr[mid] > arr[mid - 1]:
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1
                
        return start



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends