class Solution {
    public int solution(int num) {
        int answer = 0;
        long num_copy = num;
        while (num_copy != 1) {
            
            if (num_copy % 2 == 0){
                num_copy /= 2;
            }
            else {
                num_copy = num_copy * 3 + 1;
            }
            answer++;
            if (answer == 500){
                answer = -1;
                break;                
            }
        }
        if (num == 1)
            answer = 0;
        
        return answer;
    }
}