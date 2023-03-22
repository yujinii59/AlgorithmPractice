package Array;

import java.util.*;
import java.util.stream.Collectors;

/*448. Find All Numbers Disappeared in an Array*/
public class no_448 {
    public static List<Integer> findDisappearedNumbers(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int val : nums) {
            set.add(val);
        }
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 1; i <= nums.length; i++) {
            if (!set.contains(i)) {
                list.add(i);
            }
        }
        return list;
    }

    public static void main(String[] args) {
        System.out.println(findDisappearedNumbers(new int[] {1,2,2,3,5,3,1}));
    }
}
