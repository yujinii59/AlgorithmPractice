package Array;

/*88. Merge Sorted Array*/
public class no_88 {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        int res = nums1.length - 1;
        while (n > 0 && m > 0) {
            if (nums1[m-1] > nums2[n-1]) {
                nums1[res] = nums1[m-1];
                m--;
            }
            else if (nums1[m-1] < nums2[n-1]) {
                nums1[res] = nums2[n-1];
                n--;
            }
            else {
                nums1[res] = nums1[m-1];
                res--;
                m--;
                nums1[res] = nums2[n-1];
                n--;
            }
            res--;
        }
        while (n > 0) {
            nums1[res] = nums2[n-1];
            n--;
            res--;
        }
    }

    public static void main(String[] args) {
        merge(new int[]{1,2,3,0,0,0}, 3, new int[]{2,5,6}, 3);
    }
}
