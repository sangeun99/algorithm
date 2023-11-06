import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        
        String s = String.valueOf(n);
        char[] c = s.toCharArray();
        Arrays.sort(c);
        
        String as = "";
        for (int i = c.length - 1; i >=0; i--){
            as += c[i];
        }
        answer = Long.parseLong(as);
        System.out.print(answer);
        return answer;
    
    }
}