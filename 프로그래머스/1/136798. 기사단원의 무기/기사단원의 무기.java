class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        // 1 ~ number 약수 개수 구하기
        for (int i = 1; i <= number; i++){
            // 약수 개수 구하기
            int count = 0;
            for (int j = 1; j <= Math.sqrt(i); j++){
                if (j * j == i){
                    count++;
                }
                 
                else if (i % j == 0) {
                    count += 2;
                }
                if (count > limit) {
                    count = power;
                    break;
                }
            }
            answer += count;
            // limit보다 개수가 크면 answer += limit
        }
        return answer;
    }
}