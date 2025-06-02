import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int i=0; i<n; i++){
            // 줄마다 생성
            Map<Long,Integer> map = new HashMap<>();

            String[] inputs = br.readLine().split(" ");
            int num = Integer.parseInt(inputs[0]);
            if (num<1){
                sb.append("SYJKGW\n");
                continue;
            } else if (num==1){
                sb.append(inputs[1]+"\n");
                continue;
            }
            //초기화
            long maxKey = Long.parseLong(inputs[1]);
            int maxValue = 1;
            // 2 이상일때
            for (int j=1; j<=num; j++){
                Long now = Long.parseLong(inputs[j]);
                if (map.containsKey(now)) {
                    int x = map.get(now);
                    x++;
                    map.put(now,x);
                    if (x>maxValue){
                        maxKey = now;
                        maxValue = x;
                    }
                } else{
                    map.put(now,1);
                }
            }

            if (maxValue>num/2){
                sb.append(maxKey+"\n");
            } else {
                sb.append("SYJKGW\n");
            }
        }
        System.out.println(sb);
    }
}