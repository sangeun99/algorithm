class Solution {
    public String solution(String s) {
        String answer = "";
        int length = s.length();
        if (length % 2 == 1) {
            int mid = length / 2;
            answer = s.substring(mid, mid + 1);
        }
        else {
            int mid = length / 2;
            answer = s.substring(mid - 1, mid + 1);
        }
        return answer;
    }
}