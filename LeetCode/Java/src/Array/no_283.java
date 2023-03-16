package Array;

/*283. Move Zeroes*/
public class no_283 {
    public void moveZeroes(int[] nums) {
        int cnt = 0;
        int length = nums.length;
        for (int i = 0; i < length; i++) {
            int num = nums[i];
            if (num == 0) {
                cnt++;
            }
            else {
                nums[i-cnt] = num;
            }
        }

        for (int j = 1; j <= cnt; j++) {
            nums[length-j] = 0;
        }
        System.gc();
    }
}
