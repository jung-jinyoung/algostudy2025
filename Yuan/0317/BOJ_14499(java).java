import java.util.*;
import java.io.*;

class Main{
    static int[] dice = new int[]{1, 3, 4, 2, 5, 6};
    static int[] dx = new int[]{0, 0, 0, -1, 1}; // Movement directions
    static int[] dy = new int[]{0, 1, -1, 0, 0}; // Movement directions
    static int[] now_num = new int[7];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] arr = new int[r][c];
        for (int i=0; i<r; i++){
            StringTokenizer st1 = new StringTokenizer(br.readLine());
            for (int j=0; j<c; j++){
                arr[i][j] = Integer.parseInt(st1.nextToken());
            }
        }

        Arrays.fill(now_num,0);

        StringTokenizer orders = new StringTokenizer(br.readLine());

        while (orders.hasMoreTokens()){
            int k = Integer.parseInt(orders.nextToken());
            int nx = x+dx[k];
            int ny = y+dy[k];

            if (nx<0 || nx>=r || ny<0 || ny>=c) continue;


            switch (k) {
                case 1:
                    // Move east
                    int temp1 = dice[0];
                    dice[0] = dice[2];
                    dice[2] = dice[5];
                    dice[5] = dice[1];
                    dice[1] = temp1;
                    break;
                case 2:
                    // Move west
                    int temp2 = dice[0];
                    dice[0] = dice[1];
                    dice[1] = dice[5];
                    dice[5] = dice[2];
                    dice[2] = temp2;
                    break;
                case 3:
                    // Move north
                    int temp3 = dice[0];
                    dice[0] = dice[3];
                    dice[3] = dice[5];
                    dice[5] = dice[4];
                    dice[4] = temp3;
                    break;
                case 4:
                    // Move south
                    int temp4 = dice[0];
                    dice[0] = dice[4];
                    dice[4] = dice[5];
                    dice[5] = dice[3];
                    dice[3] = temp4;
                    break;
            }
            int top = dice[0];
            int bottom = dice[5];

            if (arr[nx][ny] ==0) {
                arr[nx][ny] = now_num[bottom];
            } else{
                now_num[bottom] = arr[nx][ny];
                arr[nx][ny] = 0;
            }

            System.out.println(now_num[top]);
            x = nx;
            y = ny;
        }

    }
}