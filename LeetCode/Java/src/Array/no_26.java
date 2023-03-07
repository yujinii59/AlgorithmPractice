package Array;

import java.util.Arrays;

/*26. Remove Duplicates from Sorted Array*/
public class no_26 {
    public static int removeDuplicates(int[] nums) {
        int prev = 1000;
        int duplicateCnt = 0;
        int i = 0;
        int length = nums.length;
        while (i < length) {
            int num = nums[i];
            if (num == prev) {
                duplicateCnt++;
            }
            else {
                nums[i-duplicateCnt] = num;
                prev = num;
            }
            i++;
        }
        System.out.println(Arrays.toString(nums));
        return length-duplicateCnt;
    }

    public static void main(String[] args) {
        System.out.println(removeDuplicates(new int[] {0,0,1,1,1,2,2,3,3,4}));
    }
}
