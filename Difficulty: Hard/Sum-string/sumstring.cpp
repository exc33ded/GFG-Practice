class Solution {
public:
    // Helper function to add two numbers represented as strings
    string getAdd(string &a, string &b) {
        string result = "";
        int i = a.size() - 1;
        int j = b.size() - 1;
        int carry = 0;
        
        // Digit-wise addition from right to left
        while (i >= 0 || j >= 0 || carry > 0) {
            int digitA = (i >= 0) ? a[i--] - '0' : 0;
            int digitB = (j >= 0) ? b[j--] - '0' : 0;
            
            int sum = digitA + digitB + carry;
            carry = sum / 10;
            result += (sum % 10) + '0'; // Append the digit
        }
        
        reverse(result.begin(), result.end()); // Reverse to get correct order
        return result;
    }
    
    // Recursive helper to validate the sum-string property
    bool helper(int idx, string &a, string &b, string &s) {
        if (idx == s.length()) return true; // Entire string processed
        else if (idx > s.length()) return false; // Out of bounds
        
        string newB = getAdd(a, b); // Compute the expected next substring
        
        int lenn = newB.length();
        string check = s.substr(idx, lenn); // Extract the next part from string
        
        if (check == newB) { // If matches, proceed recursively
            if (idx + lenn == s.length()) return true; // Reached the end
            if (helper(idx + lenn, b, newB, s)) return true; // Check next pair
            else return false;
        }
        
        return false; // Mismatch found
    }
    
    // Main function to check if the string is a sum-string
    bool isSumString(string &s) {
        int n = s.length();
        
        // Try all possible starting splits (a and b)
        for (int i = 1; i <= n - 2; ++i) { // Length of first substring (a)
            for (int j = 1; j <= n - i - 1; ++j) { // Length of second substring (b)
                string a = s.substr(0, i);
                string b = s.substr(i, j);
                
                // Skip numbers with leading zeros (unless it's "0")
                if ((a.size() > 1 && a[0] == '0') || (b.size() > 1 && b[0] == '0'))
                    continue;
                
                if (helper(i + j, a, b, s)) return true; // Check if valid
            }
        }
        
        return false; // No valid split found
    }
};