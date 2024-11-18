//{ Driver Code Starts
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine()); // Number of test cases
        while (tc-- > 0) {
            String[] inputLine = br.readLine().split(" ");
            int[] arr = new int[inputLine.length];
            for (int i = 0; i < inputLine.length; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            int N = arr.length;
            Solution ob = new Solution();
            ob.nextPermutation(arr); // Generate the next permutation
            StringBuilder out = new StringBuilder();
            for (int i = 0; i < N; i++) {
                out.append(arr[i] + " "); // Corrected: use arr[i] instead of arr.get(i)
            }
            System.out.println(out.toString().trim()); // Print the output
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
     void nextPermutation(int[] arr) {
        // code here
        int i = 0;
        int j = 0;
        for(i = arr.length-2;i>=0;)
        {
            if(arr[i]>=arr[i+1])
            {
                i--;
            }
            else
            {
                break;
            }
        }
        if(i>=0)
        {
            for(j = arr.length-1;j>=0;)
            {
                if(arr[j]<=arr[i])
                {
                    j--;
                }
                else
                {
                    break;
                }
            }
             int temp = arr[i];
             arr[i] = arr[j];
             arr[j] = temp;
        }
        
        reverse(arr,i+1);
    }
    void reverse(int[] arr,int idx)
    {
        int i = idx;
        int j = arr.length - 1;
        while(i<j)
        {
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }
}