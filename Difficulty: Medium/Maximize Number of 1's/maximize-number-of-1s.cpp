class Solution {
  public:
    int maxOnes(vector<int>& arr, int k) {
        // code here
        int l = 0, r = 0, maxi = 0, n = arr.size(), zeros = 0;
        while (r < n){
            if (arr[r] == 0) zeros++;
            if (zeros > k){
                if (arr[l] == 0) zeros--;
                l++;
            }
            if (zeros <= k) maxi = max(maxi, r-l+1);
            r++;
        }
        return maxi;
    }
};