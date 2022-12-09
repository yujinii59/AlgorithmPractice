import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<Integer> miro = Arrays.asList(br.readLine().split(" ")).stream().map(Integer::parseInt).collect(Collectors.toList());
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0});
        int[] visited = new int[n];
        int answer = -1;
        while (true){
             int[] val = queue.poll();
             if (val == null) break;
             int cnt = val[0];
             int num = val[1];
             if (num == n-1) {
                 answer = cnt;
                 break;
             }

             for (int i = 0; i < Math.min(miro.get(num), n-num-1); i++){
                 if (miro.get(num+i+1) != 0 & visited[num+i+1] == 0){
                     queue.offer(new int[]{cnt+1, num+i+1});
                     visited[num+i+1] = 1;
                 }
             }
         }
        System.out.println(answer);

    }
}
