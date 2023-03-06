package Array;

import java.util.Arrays;

/*1089. Duplicate Zeros*/
public class no_1089 {
    public static void duplicateZeros(int[] arr) {
        int i = 0;
        int length = arr.length;
        int j = 1;
        while (i < length) {
            int num = arr[i];
            if (num == 0 && i+1 < length) {
                for (int k = length-1; k > i+1; k--) {
                    arr[k] = arr[k-1];
                }
                arr[i+1] = 0;
                i++;
                j++;
            }
            i++;
        }
        System.out.println(Arrays.toString(arr));
    }


    public static void main(String[] args) {
        duplicateZeros(new int[]{1,0,2,3,0,4,5,0});
    }
}
