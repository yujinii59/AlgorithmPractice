package Array;

import java.util.Arrays;

/*977. Squares of a Sorted Array*/
public class no_977 {
    public static int[] sortedSquares(int[] nums) {
        int[] rst = new int[nums.length];
        int[] absNums = new int[10001];
        for (int num : nums) {
            absNums[Math.abs(num)]++;
        }
        int i = 0;
        for (int j = 0; j < 10001; j++) {
            int cnt = absNums[j];
            if (cnt > 0) {
                int square = (int) Math.pow(j, 2);
                while (cnt > 0) {
                    rst[i] = square;
                    i++;
                    cnt--;
                }
            }
        }

        return rst;
    }

    public static void main(String[] args) {
        System.out.println(Math.pow(2, 10));
        System.out.println(Arrays.toString(sortedSquares(new int[]{-4, -1, 0, 3, 10})));
    }
}
