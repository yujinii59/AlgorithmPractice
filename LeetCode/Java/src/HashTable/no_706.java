package HashTable;

import java.util.HashMap;
import java.util.Map;

/*706. Design HashMap*/
public class no_706 {
    Map<Integer, Integer> map;

    public no_706() {
        this.map = new HashMap<>();
    }

    public void put(int key, int value) {
        this.map.put(key, value);
    }

    public int get(int key) {
        return this.map.getOrDefault(key, -1);
    }

    public void remove(int key) {
        this.map.remove(key);
    }
}
