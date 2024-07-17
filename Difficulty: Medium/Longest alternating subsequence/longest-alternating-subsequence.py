#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, nums):
       #code here
        positives=0
        negatives=0
        ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>ans:
                positives=negatives+1
                ans=nums[i]
            elif nums[i]<ans:
                negatives=positives+1
                ans=nums[i]
        return max(positives,negatives)+1


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends