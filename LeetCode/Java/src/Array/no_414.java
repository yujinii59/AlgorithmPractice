package Array;

import java.util.ArrayList;
import java.util.Set;
import java.util.TreeSet;

/*414. Third Maximum Number*/
public class no_414 {
    public static int thirdMax(int[] nums) {
        Set<Integer> set = new TreeSet<>();
        for (int num : nums) {
            set.add(num);
        }
        ArrayList<Integer> list = new ArrayList<>(set);
        if (list.size() < 3) return list.get(list.size()-1);

        return list.get(list.size()-3);
    }

    public static void main(String[] args) {
        System.out.println(thirdMax(new int[] {2,1}));
    }
}
