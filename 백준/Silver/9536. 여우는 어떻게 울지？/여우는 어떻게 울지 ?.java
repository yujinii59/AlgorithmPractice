import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        for (int i=0; i < t; i++){
            String[] sounds = br.readLine().split(" ");

            Set<String> set = new HashSet<String>();
            while (true){
                String str = br.readLine();
                if (str.equals("what does the fox say?")) break;
                String[] animals = str.split(" ");
                set.add(animals[animals.length-1]);
            }

            for (String sound: sounds){
                if (!set.contains(sound)) {
                    System.out.print(sound+" ");
                }
            }
        }
    }

}
