import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        // int[] arr = {4, 6, 8, 1, 10, 56, 7865, 2, 234, 5};
        
        int[] answer = {};
        ArrayList<Integer> answerL = new ArrayList<Integer>();
        boolean[] b = new boolean [arr.length];
        for (int i = 0; i < arr.length; i++)
            b[i] = false;
        int min = arr[0];
        int minIndex = 0;
        b[0] = true;
        for (int i = 0; i < arr.length; i++){
            if (min > arr[i]){
                b[minIndex] = false;
                min = arr[i];
                minIndex = i;
                b[minIndex] = true;
            }
        }
        
        for (int i = 0; i < b.length; i++){
            if (!b[i]) {
                answerL.add(arr[i]);
            }
        }
        
        if (answerL.isEmpty())
            answerL.add(-1);   
        answer = answerL.stream().mapToInt(i->i).toArray();
        
        return answer;
    }
}