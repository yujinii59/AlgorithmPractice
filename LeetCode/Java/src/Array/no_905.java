package Array;

import java.util.Arrays;

/*905. Sort Array By Parity*/
public class no_905 {
    public static int[] sortArrayByParity(int[] nums) {
        int[] rst = new int[nums.length];
        int[] odd = new int[nums.length];
        int idx = 0;
        int odd_idx = 0;
        for (int num: nums) {
            if (num % 2 == 0) {
                rst[idx++] = num;
            } else {
                odd[odd_idx++] = num;
            }
        }

        for (int j = 0; j < odd_idx; j++){
            rst[idx++] = odd[j];
        }

        return rst;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(sortArrayByParity(new int[]{3, 1, 2, 4})));
    }
}
