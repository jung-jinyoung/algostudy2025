import java.util.*;
import java.io.*;
/*
1-0 bfs시
 가중치 낮은 방문이 우선
 x-1의 경우 분기점이 더 빨리 생김
 순서는 2*0 -> x-1 -> x+1 순으로 가야함
 */

class Main{
    static int n,k;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        n = Integer.parseInt(inputs[0]);
        k = Integer.parseInt(inputs[1]);

//        Set<Integer> s = new HashSet<>();
        Boolean[] arr = new Boolean[100001];
        Arrays.fill(arr,false);

        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{n,0});
//        s.add(n);
        arr[n] = true;

        while (!q.isEmpty()){
            int[] now = q.pollFirst();
            int now_x = now[0];
            int now_t = now[1];
            if (now_x == k){
                System.out.println(now_t);
                return;
            }
            if (0<=(now_x*2) && (now_x*2)<100001 && !arr[now_x*2]){
                q.add(new int[]{now_x *2, now_t});
                arr[now_x*2] = true;
            }
            if (0<=(now_x+1) && (now_x+1)<100001 && !arr[now_x+1]){
                q.add(new int[]{now_x + 1, now_t + 1});
                arr[now_x+1] = true;
            }
            if (0<=(now_x-1) && (now_x-1)<100001 && !arr[now_x-1]){
                q.add(new int[]{now_x - 1, now_t + 1});
                arr[now_x-1] = true;
            }

        }


    }
}