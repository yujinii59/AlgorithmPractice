package BinarySearch;

/*704. Binary Search*/
public class no_704 {
    public static int binarySearch(int[] nums, int target, int start, int end) {
        if (start > end) return -1;
        else if (start == end) {
            if (start == nums.length || nums[start] != target) return -1;
            else return start;
        }
        else {
            int mid = (start + end) / 2;
            if (nums[mid] > target) return binarySearch(nums, target, start, mid);
            else if (nums[mid] < target) return binarySearch(nums, target, mid+1, end);
            else return mid;
        }
    }

    public static int search(int[] nums, int target) {
        return binarySearch(nums, target, 0, nums.length);
    }

    public static void main(String[] args) {
        System.out.println(search(new int[] {-1,0,3,5,9,12}, 2));
    }
}
