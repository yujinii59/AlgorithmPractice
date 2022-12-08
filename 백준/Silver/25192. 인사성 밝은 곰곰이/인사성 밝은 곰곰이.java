import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String args[]) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());
        Set<String> set = new HashSet<String>();
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
//            System.out.println(st.nextToken().toString().equals("ENTER"));
            String str = st.nextToken().toString();
            if (str.equals("ENTER")) {
                set.clear();
            }else{
                if (!set.contains(str)) {
                    set.add(str);
                    cnt++;
                }
            }
        }
        System.out.println(cnt);
    }
}
