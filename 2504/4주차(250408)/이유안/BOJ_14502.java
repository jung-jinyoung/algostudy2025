/*
n m 직사각형
0 빈칸 1 벽 2바이러스
벽 3개 세우고 바이러스 퍼트린 다음에 안전영역 구하기
 */

import java.util.*;
import java.io.*;
class Main{
    static int r,c;
    static int[] dx = new int[]{1, -1, 0, 0};
    static int[] dy = new int[]{0, 0, 1, -1};
    static int[][] arr;
    static int res;
    static List virus,lst;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        r = Integer.parseInt(inputs[0]);
        c = Integer.parseInt(inputs[1]);
        arr = new int[r][c];

//        ArrayDeque q = new ArrayDeque();
        lst = new ArrayList();
        virus = new ArrayList();

        for (int i=0; i<r; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0; j<c; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (arr[i][j] ==0){ // 빈칸
                    lst.add(new int[]{i, j});
                } else if(arr[i][j] ==2){ // 바이러스
                    virus.add(new int[]{i, j});
                }
            }
        }
//        for (int[]ar: arr){
//            System.out.println(Arrays.toString(ar));
//        }
        // lst 중에 3개 돌기
        int n = lst.size();
//        System.out.println("벽 개수:"+n);
        for (int x=0; x<(n-2); x++){
            for (int y=(x+1); y<(n-1); y++){
                for (int z=(y+1); z<n; z++){
                    int[] o1 = ((int[]) lst.get(x));
                    int[] o2 = ((int[]) lst.get(y));
                    int[] o3 = ((int[]) lst.get(z));
                    int[][] visit = new int[r][c];
                    // 벽 세우기
//                    int [][] newarr = arr.clone();
                    int[][] newarr = new int[r][c];
                    for (int c=0; c<r; c++){
                        newarr[c] = arr[c].clone();
                    }
                    newarr[o1[0]][o1[1]] = 1;
                    newarr[o2[0]][o2[1]] = 1;
                    newarr[o3[0]][o3[1]] = 1;
                    visit[o1[0]][o1[1]] = 1;
                    visit[o2[0]][o2[1]] = 1;
                    visit[o3[0]][o3[1]] = 1;
                    check(newarr, visit);
                }
            }
        }
        System.out.println(res);

    }

    public static void check(int[][] newarr, int[][] visit) {
        int total = 0;
        ArrayDeque q = new ArrayDeque();
//        System.out.println(virus.size());
        for (int c=0; c<virus.size(); c++){
            int[] vi = ((int[])virus.get(c));
            q.add(new int[]{vi[0], vi[1]});
        }
//        System.out.println("q:"+q);
        // 벽 제외하고 바이러스 퍼트리기
        while (!q.isEmpty()){
            int now[] = ((int[]) q.pollFirst());
            int x = now[0];
            int y = now[1];
            for (int k=0; k<4; k++){
                int nx = x+dx[k];
                int ny = y+dy[k];
                if (0<=nx && nx<r && 0<=ny && ny<c && newarr[nx][ny]==0 && visit[nx][ny] ==0){
                    visit[nx][ny] = 1;
                    newarr[nx][ny] = 2;
                    q.add(new int[]{nx, ny});
                }
            }
        }
//        System.out.println("update");
//        for(int[] ar: newarr){
//            System.out.println(Arrays.toString(ar));
//        }
//        System.out.println("----------------------");
        // 안전영역 개수세기
        for (int i=0; i<r; i++){
            for (int j=0; j<c; j++){
                if (newarr[i][j] == 0) total++;
            }
        }
//        System.out.println("total:"+total);
        if (total>res) {

            res=total;
        }

    }
}