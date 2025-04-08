import java.util.*;
import java.io.*;

class Main{
    static int t;
    static int[] dx = new int[]{0,0,1,-1};
    static int[] dy = new int[]{1,-1,0,0};
    static int[][][] visit;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++){
            String[] inputs = br.readLine().split(" ");
            int c = Integer.parseInt(inputs[0]);
            int r = Integer.parseInt(inputs[1]);

            String[][] arr = new String[r][c];
            //        visit에 [ [], [], [], [], ... ] r개 넣어주기
            visit = new int[r][c][2];
            ArrayDeque<String[]> q = new ArrayDeque<>();
            String nowr="";
            String nowc="";
            for (int x=0; x<r; x++){
                String[] its = br.readLine().split("");
//                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int y=0; y<c; y++){
                    arr[x][y] = its[y];
                    if (arr[x][y].equals("@")) {
                        visit[x][y][1] = 1; // 내위치
                        nowr = Integer.toString(x);
                        nowc = Integer.toString(y);
                    } else if (arr[x][y].equals("*")){
                        visit[x][y][0] = -1; // 불
                        q.add(new String[]{Integer.toString(x),Integer.toString(y),"*"});
                    }
                }
            }
            q.add(new String[]{nowr, nowc,"@"});
            find(q, arr, r, c);
        }
    }
    public static void find(ArrayDeque q, String[][] arr, int r, int c){
        while (!q.isEmpty()){
            String[] now = (String[]) q.pollFirst();
            int x = Integer.parseInt(now[0]);
            int y = Integer.parseInt(now[1]);
            String me = now[2];
//          현위치 체크
            if (x==(r-1) || x==0 || y == (c-1) || y ==0){
                if (me.equals("@")){
                System.out.println(visit[x][y][1]);
                return;
                }
            }
//          이동
            for (int k=0; k<4; k++){
                int nx = x+dx[k];
                int ny = y+dy[k];
                if (0<=nx && nx<r && 0<=ny && ny<c){
                // 불 일때: 불 안남, 별 아님
                    if( me.equals("*") && visit[nx][ny][0]!=-1 && !arr[nx][ny].equals("#") ){
                        visit[nx][ny][0] = -1;
                        q.add(new String[]{Integer.toString(nx), Integer.toString(ny),"*"});
                    }
                // 내 위치: 불 안남, 방문안함, 통로
                    else if( me.equals("@") && visit[nx][ny][0]!=-1 && visit[nx][ny][1]==0 && arr[nx][ny].equals(".") ){
                        visit[nx][ny][1] = visit[x][y][1]+1;
                        q.add(new String[]{Integer.toString(nx), Integer.toString(ny),"@"});
                    }
                }

            }

        }
        System.out.println("IMPOSSIBLE");
    }
}