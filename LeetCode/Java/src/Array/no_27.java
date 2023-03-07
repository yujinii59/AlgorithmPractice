package Array;

import java.util.Arrays;

/*27. Remove Element*/
public class no_27 {
    public static int removeElement(int[] nums, int val) {
        int i = 0;
        int j = 0;
        int length = nums.length;
        while (i < length) {
            int num = nums[i];
            if (num == val) {
                j++;
            } else {
                nums[i-j] = num;
            }
            i++;
        }
        return length-j;
    }

    public static void main(String[] args) {
        System.out.println(removeElement(new int[] {3,2,2,3}, 3));
    }
}
