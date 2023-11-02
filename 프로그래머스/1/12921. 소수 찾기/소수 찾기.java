class Solution {
    public int solution(int n) {
        int answer = 0;
        // 2부터 n까지 소수의 개수 구하기
        for (int i = 2; i <= n; i++){
            answer++;
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0){
                    answer--;
                    break;                    
                }
            }
        }
        return answer;
    }
}