package Array;

/*941. Valid Mountain Array*/
public class no_941 {

    public static boolean validMountainArray(int[] arr) {
        int length = arr.length;
        if (length < 3) return false;
        int prev = arr[0];
        int sign = 0;
        for (int i=1; i < length; i++) {
            int num = arr[i];
            if (sign == 0 && prev >= num) return false;
            else if (sign == -1 && prev < num) return false;
            else {
                if (prev > num) {
                    sign = -1;
                }
                else if (prev < num) {
                    sign = 1;
                }
                else {
                    return false;
                }
            }
            prev = num;
        }
        return sign != 1;
    }

    public static void main(String[] args) {
        System.out.println(validMountainArray(new int[] {0,3,2,1}));
    }

}
