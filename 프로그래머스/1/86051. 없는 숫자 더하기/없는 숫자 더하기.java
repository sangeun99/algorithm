class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        boolean[] n = new boolean[10];
        for (int i = 0; i < 10; i++)
            n[i] = false;
        for (int i = 0; i < numbers.length; i++){
            n[numbers[i]] = true;
        }
        for (int i = 0; i < 10; i++)
            if (!n[i]) {
                answer += i;
            }
        return answer;
    }
}