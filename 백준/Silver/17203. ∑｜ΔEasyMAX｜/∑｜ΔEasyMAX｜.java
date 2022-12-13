import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] rapid = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
        int[] amount = new int[n-1];
        for (int i = 0; i < n-1; i++){
            if (i == 0){
                amount[i] = Math.abs(rapid[i] - rapid[i+1]);
            }else{
                amount[i] = amount[i-1] + Math.abs(rapid[i] - rapid[i+1]);
            }
        }

        for (int j = 0; j < m; j++){
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            if (e <= s){
                System.out.println(0);
            }else{
                if (s==1){
                    System.out.println(amount[e-2]);
                }else{
                    System.out.println(amount[e-2] - amount[s-2]);
                }
            }
        }
    }
}
