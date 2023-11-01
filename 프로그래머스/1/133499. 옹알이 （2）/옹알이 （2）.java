class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        for (String item: babbling) {
            String lastword = "";
            for (int i = 0; i < item.length();){
                String temp = item.substring(i);
                if (temp.startsWith("aya") && !lastword.equals("aya")) {
                    i += 3;
                    lastword = "aya";
                }
                else if (temp.startsWith("woo") && !lastword.equals("woo")) {
                    i += 3;
                    lastword = "woo";
                }
                else if (temp.startsWith("ye") && !lastword.equals("ye")) {
                    i += 2;
                    lastword = "ye";
                }
                else if (temp.startsWith("ma") && !lastword.equals("ma")) {
                    i += 2;
                    lastword = "ma";
                }
                else {
                    break;
                }
                if (i == item.length()) {
                    answer += 1;
                }
            }         
        }
        return answer;
    }
}