class Solution:
    def minSoldiers(self, arr, k):
        a=[]
        count=0
        sum=0
        for i in range(len(arr)):
            if arr[i]%k == 0:
                count+=1
            else:
                a.append(k-arr[i]%k)
        a.sort()
        if len(arr)%2==0:
            l=len(arr)//2
        else:
            l=len(arr)//2 +1
        for i in range(l-count):
            sum+=a[i]
        return sum