import java.util.*;
import java.io.*;
class Main{
    static int n;
    static int[][] arr;
    static boolean[][] visited;
    static int[]dx = new int[]{1,-1,0,0};
    static int[]dy = new int[]{0,0,1,-1};
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        visited = new boolean[n][n];

        for (int r=0; r<n; r++){
            String[] inputs = br.readLine().split("");
            for (int c=0; c<n; c++){
                arr[r][c] = Integer.parseInt(inputs[c]);
            }
        }
//        StringBuilder sb = new StringBuilder();
        List<Integer> res = new ArrayList<>();

        int cnt = 0;
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                // 1이고 방문 안했을 때 bfs시작
                if (arr[i][j] == 1 && !visited[i][j]){
                    cnt++; // 단지 개수 추가 해주기
                    visited[i][j] = true;
                    ArrayDeque<int[]> q = new ArrayDeque<>();
                    q.add(new int[]{i, j}); // 현위치
                    int now_cnt = bfs(q);
                    res.add(now_cnt);
                }
            }
        }
        System.out.println(cnt);
        Collections.sort(res);
        for (int r:res){
            System.out.println(r);
        }
    }

    static int bfs(ArrayDeque q){
        int now_cnt = 1; // 시작 단지
        while (!q.isEmpty()){
            int[] now = ((int[])q.pollFirst());
            int x = now[0];
            int y = now[1];
            for (int k=0; k<4; k++){
                int nx = x+dx[k];
                int ny = y+dy[k];
                //0,n 범위안, not visit, arr[nx][ny] = 1
                if (0<=nx && nx<n && 0<=ny && ny<n && !visited[nx][ny] && arr[nx][ny] ==1){
                    visited[nx][ny] = true;
                    now_cnt++;
                    q.add(new int[]{nx, ny});
                }
            }

        }

        return now_cnt;
    }
}