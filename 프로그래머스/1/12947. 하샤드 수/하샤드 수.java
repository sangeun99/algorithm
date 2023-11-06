class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        // 자릿수의 합 구하기
        int sum = 0;
        int x_copy = x;
        while (x_copy > 0) {
            sum += x_copy % 10;
            x_copy /= 10;
        }
        
        if (x % sum != 0)
            answer = false;
        return answer;
    }
}