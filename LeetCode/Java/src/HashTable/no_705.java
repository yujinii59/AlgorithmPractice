package HashTable;

import java.util.HashSet;
import java.util.Set;

/*705. Design HashSet*/
public class no_705 {
    Set<Integer> set;

    public no_705() {
        this.set = new HashSet<>();
    }

    public void add(int key) {
        this.set.add(key);
    }

    public void remove(int key) {
        this.set.remove(key);
    }

    public boolean contains(int key) {
        return this.set.contains(key);
    }
}
