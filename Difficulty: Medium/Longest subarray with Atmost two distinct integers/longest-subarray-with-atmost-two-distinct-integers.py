class Solution:
    def totalElements(self, arr):
        # Code here
        maxi=float('-inf')
        right=0
        one=arr[0]
        left=0
        while right<len(arr):
            while right<len(arr) and arr[right]==one:
                right+=1
            break
        if right<len(arr):
            two=arr[right] 
        else:
            return right
        mid=right
        midel=arr[right]
        while right<len(arr):
            if arr[right]==one:
                if arr[right]!=midel:
                    mid=right
                    midel=arr[right]
                right+=1
            elif arr[right]==two:
                if arr[right]!=midel:
                    mid=right
                    midel=arr[right]
                right+=1
            else:
                maxi=max(maxi,right-left)
                left=mid
                one=arr[left]
                two=arr[right]
        maxi=max(maxi,right-left)   
        return maxi