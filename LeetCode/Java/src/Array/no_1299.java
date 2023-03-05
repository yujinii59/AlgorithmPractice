package Array;

import java.util.Arrays;

/*1299. Replace Elements with Greatest Element on Right Side*/
public class no_1299 {
    public static int[] replaceElements(int[] arr) {
        int length = arr.length;
        int[] rst = new int[length];
        int prev = -1;
        for (int i=length-1; i >= 0; i--) {
            rst[i] = prev;
            if (arr[i] > prev){
                prev = arr[i];
            }
        }

        return rst;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(replaceElements(new int[]{17, 18, 5, 4, 6, 1})));
    }
}
