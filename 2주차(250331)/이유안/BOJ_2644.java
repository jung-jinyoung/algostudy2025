import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

class Main{
    static int n;
    static int n1,n2;
    static ArrayList[] graph;
    static Boolean [] visit;
    static int minV = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        // 이중배열로 초기화
        graph = new ArrayList[(n+1)];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        String[] input = br.readLine().split(" ");
        n1 = Integer.parseInt(input[0]);
        n2 = Integer.parseInt(input[1]);

        int m = Integer.parseInt(br.readLine());
        for (int i=0; i<m; i++){
            String[] inp = br.readLine().split(" ");
            int x = Integer.parseInt(inp[0]);
            int y = Integer.parseInt(inp[1]);
            graph[x].add(y);
            graph[y].add(x);
        }
        visit = new Boolean [(n+1)];
        Arrays.fill(visit, false);
        dfs(n1,0,graph); // 시작노드,촌수계산,

        if (minV == Integer.MAX_VALUE){
            System.out.println(-1);
        }else{
            System.out.println(minV);
        }
    }
    static void dfs(int now, int cnt, ArrayList<Integer>[] graph){
        if (now == n2){
            minV = Math.min(cnt, minV);
            return;
        }
        for (int nxt: graph[now]){
            if (!visit[nxt]){
                visit[nxt] = true;
                dfs(nxt,cnt+1,graph);
                visit[nxt] = false;
            }
        }

    }
}