class Solution {
  public:
    int kthSmallest(vector<vector<int>> &matrix, int k) {
        // code here
        int n = matrix.size();
        int low = matrix[0][0];
        int high = matrix[n-1][n-1];
    
        while (low < high) {
            int mid = low + (high - low) / 2;
            int count = 0;
            int row = n - 1, col = 0;
    
            while (row >= 0 && col < n) {
                if (matrix[row][col] <= mid) {
                    count += (row + 1);
                    col++;
                } else {
                    row--;
                }
            }
    
            if (count < k) {
                low = mid + 1;  // kth element is bigger
            } else {
                high = mid;     // kth element is smaller or equal
            }
        }
    
        return low;
    }
};

