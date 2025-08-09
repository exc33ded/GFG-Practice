class Solution {
    int getLongestPrefix(String s) {
        int prefix = 0;
        int suffix = 1;
        int count = 0;
        int pos = 1;

        while (prefix<s.length() && suffix<s.length()){
            if(s.charAt(prefix)==s.charAt(suffix)){
                prefix++;
                suffix++;
                count++;
            }else{
                prefix = 0;
                pos++;
                suffix = pos;
                count = 0;
            }
        }

        if (count>0){
            int length = s.length()-1;
            while (true){
                String str = s.substring(0,length)+s.substring(0,length);
                if(str.startsWith(s)){
                    return length;
                }
                length--;
            }
        }
        return -1;
    }
}