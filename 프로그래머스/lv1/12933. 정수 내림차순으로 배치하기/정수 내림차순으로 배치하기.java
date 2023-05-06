import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        String str = Long.toString(n);
        char[] c = str.toCharArray();
        Arrays.sort(c);

        str = new StringBuilder(new String(c)).reverse().toString();

        System.out.println(str);
        answer = Long.parseLong(str);
        return answer;
    }
}