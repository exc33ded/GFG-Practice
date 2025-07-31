#include <vector>
#include <string>
#include <unordered_map>

// User function Template for C++

class Solution {
public:
    /**
     * @brief Checks if a character is a vowel.
     * @param c The character to check.
     * @return True if the character is a vowel, false otherwise.
     */
    bool isVowel(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }

    /**
     * @brief Counts the number of contiguous subarrays of strings that, when concatenated,
     * form a balanced string (equal vowels and consonants).
     * @param arr The input vector of strings.
     * @return The total count of such balanced subarrays.
     *
     * @details
     * The problem is equivalent to finding the number of contiguous subarrays
     * whose cumulative sum of (vowels - consonants) is zero.
     *
     * This can be solved efficiently in O(N) time using a hash map and prefix sums,
     * where N is the total number of characters in all strings.
     *
     * 1. First, the input `arr` of strings is transformed into an integer array `diff`,
     * where `diff[i] = count_vowels(arr[i]) - count_consonants(arr[i])`.
     *
     * 2. We then iterate through the `diff` array, maintaining a running `prefix_sum`.
     *
     * 3. A hash map `prefix_sum_counts` stores the frequency of each prefix sum encountered.
     * We initialize it with {0, 1} to handle subarrays that start from index 0.
     *
     * 4. If we encounter a `prefix_sum` that is already in the map, it means the
     * subarray(s) between the previous occurrence(s) and the current position have a
     * sum of zero. We add the stored frequency to our total count.
     *
     * 5. Finally, we update the frequency of the current `prefix_sum` in the map.
     */
    long long countBalanced(std::vector<std::string>& arr) {
        int n = arr.size();
        std::vector<int> diff(n);

        // 1. Transform the string array into a difference array.
        for (int i = 0; i < n; ++i) {
            int vowels = 0;
            for (char c : arr[i]) {
                if (isVowel(c)) {
                    vowels++;
                }
            }
            int consonants = arr[i].length() - vowels;
            diff[i] = vowels - consonants;
        }

        // 2. Use a hash map to count subarrays with a sum of zero.
        std::unordered_map<long long, long long> prefix_sum_counts;
        prefix_sum_counts[0] = 1; // Base case for subarrays starting at index 0.

        long long prefix_sum = 0;
        long long total_balanced_count = 0;

        for (int val : diff) {
            prefix_sum += val;

            // If this prefix_sum has been seen before, it means the subarray
            // between the previous occurrences and now has a sum of 0.
            if (prefix_sum_counts.count(prefix_sum)) {
                total_balanced_count += prefix_sum_counts[prefix_sum];
            }

            // Increment the count for the current prefix_sum.
            prefix_sum_counts[prefix_sum]++;
        }

        return total_balanced_count;
    }
};