package Sorting;

import java.util.Arrays;

/*1051. Height Checker*/
public class no_1051 {

    public static int heightChecker(int[] heights) {
        int[] sorted = Arrays.stream(heights).sorted().toArray();
        int cnt = 0;
        for (int i=0; i < heights.length; i++) {
            if (sorted[i] != heights[i]) cnt++;
        }
        return cnt;
    }

    public static void main(String[] args) {
        System.out.println(heightChecker(new int[] {1,1,4,2,1,3}));
    }
}
