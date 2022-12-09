import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++){
            int cnt = 0;
            int one = 0;
            String[] nums = br.readLine().split(" ");
            String num1 = nums[0];
            String num2 = nums[1];
            for (int j = 0; j < num1.length(); j++){
                if (num1.charAt(j) != num2.charAt(j)){
                    if (num1.charAt(j) == '1' & one > 0){
                        one--;
                    }else if (num2.charAt(j) == '1' & one < 0){
                        one++;
                    }else{
                        cnt++;
                        if (num1.charAt(j) == '1') one--;
                        else one++;
                    }
                }

            }
            System.out.println(cnt);
        }

    }
}
