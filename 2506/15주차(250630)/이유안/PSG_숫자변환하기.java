import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        // int answer = -1;
        int[] visit = new int[1000001];
        return bfs(x,y,n,visit);
    }
    public static int bfs(int x , int y, int n, int[] visit){
        ArrayDeque q = new ArrayDeque<>();
        visit[x] = 1;
        q.add(new int[]{x,0});
        while (!q.isEmpty()){
            int[] now= (int[]) q.pollFirst(); 
            int p = now[0]; 
            int c = now[1]; 
            // System.out.println(p);
            if (p==y) return c; 
            if ((p+n)<=y && visit[(p+n)] == 0){
                q.add(new int[]{(p+n),c+1});
                visit[(p+n)] = 1;
            }
            if ((p*2)<=y && visit[(p*2)] == 0){
                q.add(new int[]{(p*2),c+1});
                visit[(p*2)] = 1; 
            }
            if ((p*3)<=y && visit[(p*3)] == 0){
                q.add(new int[]{(p*3),c+1});
                visit[(p*3)] = 1;
            }
        }
        
        return -1;
    }
}