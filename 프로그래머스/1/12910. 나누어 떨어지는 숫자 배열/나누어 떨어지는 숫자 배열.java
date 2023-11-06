import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        
        ArrayList<Integer> answerL = new ArrayList<Integer>();
        for (int item: arr){
            if (item % divisor == 0) {
                answerL.add(item);
            }
        }
        if (answerL.isEmpty()){
            answerL.add(-1);
        }
        System.out.print(answerL);
        
        int[] answer = answerL.stream()
                        .mapToInt(i->i)
                        .sorted()
                        .toArray();
        return answer;
    }
}