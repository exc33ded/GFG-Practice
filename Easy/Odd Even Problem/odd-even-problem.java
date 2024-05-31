//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while (t-- > 0) {

            String s;
            s = br.readLine();

            Solution obj = new Solution();
            String res = obj.oddEven(s);

            System.out.println(res);
        }
    }
}

// } Driver Code Ends



class Solution {
    static boolean isEven(int n){
       if((n&1)==0)
       return true;
       else
       return false;
   }
   
   static String oddEven(String S) {
       
       
       HashMap<Character,Integer> h=new HashMap<>();
       
       for(int i=0;i<S.length();i++){
           h.put(S.charAt(i),h.getOrDefault(S.charAt(i),0)+1);
       }
       
       int X=0;
       int Y=0;
       
       for(Map.Entry<Character,Integer> entry : h.entrySet()){
       
           int characterPos=(int)entry.getKey() - 64;
           int characterFrequency=entry.getValue();
           
           if(isEven(characterPos) && isEven(characterFrequency))
            X++;
           if(!isEven(characterPos) && !isEven(characterFrequency)) 
           Y++;
       }
       
       int z=X+Y;
       
       if(isEven(z))
       return "EVEN";
       else
       return "ODD";
       
   }

 
}
