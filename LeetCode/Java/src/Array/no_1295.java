package Array;

/*1295. Find Numbers with Even Number of Digits*/
public class no_1295 {
    public static int findNumbers(int[] nums) {
        int rst = 0;
        for (int num : nums) {
            if(Integer.toString(num).length() % 2 == 0) {
                rst++;
            }
        }

        return rst;
    }

    public static void main(String[] args) {
        System.out.println(findNumbers(new int[]{555,901,482,1771}));
    }
}
