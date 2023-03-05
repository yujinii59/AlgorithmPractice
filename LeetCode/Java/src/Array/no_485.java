package Array;

/*485. Max Consecutive Ones*/
public class no_485 {
    public static int findMaxConsecutiveOnes(int[] nums) {
        int rst = 0;
        int count = 0;
        for (int num : nums) {
            if (num == 1) {
                count++;
            }
            else {
                rst = Math.max(rst, count);
                count = 0;
            }
        }
        rst = Math.max(rst, count);
        return rst;
    }

    public static void main(String[] args) {
        System.out.println(findMaxConsecutiveOnes(new int[]{1,1,0,1,1,1}));
    }
}
