import java.sql.Array;
import java.sql.SQLOutput;
import java.util.*;
import java.io.*;

class Main {
    static int n;
    static int[][] arr;
    static int[] dx = new int[]{1, -1, 0, 0};
    static int[] dy = new int[]{0, 0, 1, -1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 안전 영역 최대개수 출력, 최소 0
        // 높이 n기준
        n = Integer.parseInt(br.readLine());
        arr = new int[n][n];
        for (int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++){
                int x = Integer.parseInt(st.nextToken());
                arr[i][j] = x;
            }
        }
        int res = 0;
        int h = 1;
        // 높이 0이면 지역1, 높이 1이면 모름...
        while (true){
            int[][] visit = new int[n][n];
            ArrayDeque<int[]> q = new ArrayDeque<>();
            // bfs 한번 돌려서 잠기기
            for (int x=0; x<n; x++){
                for (int y=0; y<n; y++){
                    if ( arr[x][y]<=h && visit[x][y]==0){
                        visit[x][y] = 1;
                        q.add(new int[]{x,y});
                        bfs(q,visit,h);
                    }
                }
            }
            for (int[] vs:visit){
                System.out.println(Arrays.toString(vs));
            }
        // bfs 두번 돌려서 안잠긴 지점 세기, 전부 잠기면 h=0
            int midcnt = 0;
            ArrayDeque<int[]> qq = new ArrayDeque<>();
            for (int x=0; x<n; x++){
                for (int y=0; y<n; y++){
                    if (visit[x][y]==0){
                        midcnt++;
                        visit[x][y] = 1;
                        qq.add(new int[]{x,y});
                        count(qq,visit);
                    }
                }
            }

            if (midcnt>0){
                if (midcnt>res){
                    res = midcnt;
                }
                h++;
            }
            else if (midcnt == 0){
                break;
            }
        }

        System.out.println(res);

    }
    public static void bfs(ArrayDeque q, int[][] visit,int h){
        while (!q.isEmpty()){
            int[] now = ((int[])q.pollFirst());
            int x = now[0];
            int y = now[1];
            for (int k=0; k<4; k++){
                int nx = x+dx[k];
                int ny = y+dx[k];
                if (0<=nx && nx<n && 0<=ny && ny<n && visit[nx][ny] ==0 && arr[nx][ny]<=h){
                    visit[nx][ny] = 1;
                    q.add(new int[]{nx, ny});
                }

        }
        }

    }
    public static void count(ArrayDeque qq, int[][] visit){
        while (!qq.isEmpty()){
            int[] now = ((int[])qq.pollFirst());
            int x = now[0];
            int y = now[1];
            for (int k=0; k<4; k++){
                int nx = x+dx[k];
                int ny = y+dy[k];
                if (0<=nx && nx<n && 0<=ny && ny<n && visit[nx][ny] ==0){
                    visit[nx][ny] = 1;
                    qq.add(new int[]{nx, ny});
                }

            }
        }

    }
}