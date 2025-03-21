//import java.io.IOException;
import java.io.*;
import java.util.*;

public class Main {
    static final int INF = (int)1e9;
    static int n,m,x;
    static List<Node>[] graph;
    // 노드 클래스 정의, Comparable 상속받음
    static class Node implements Comparable<Node> {
        int dest, cost;
        public Node(int dest, int cost){
            this.dest = dest;
            this.cost = cost;
        }
        // pq의 기준 생성: 오름차순
        @Override
        public int compareTo(Node o){
            return this.cost - o.cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        List<Node>[] graph = new ArrayList[n+1];
        for (int i=0; i<(n+1); i++){
            graph[i] = new ArrayList<>();
        }
        // m 줄 반복
        for (int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            graph[s].add(new Node(e, c));
        }
        // x에서 이동 시작하는 최단거리 배열
        int[] XtoN = diks(x, n, graph);
        int res = 0;

        for ( int i=1; i<(n+1); i++){
            if (i==x) continue;
            int[] nowdis = diks(i, n, graph);

            int nowres = nowdis[x] + XtoN[i];
            if (nowres >res) res = nowres;
        }
        System.out.println(res);

    }

    static int[] diks(int start, int n, List<Node>[] graph){
        PriorityQueue<Node> pq = new PriorityQueue<>();
        // 노드마다 최소비용 저장할 배열 생성, 최대값으로 초기화
        int[] dist = new int[n+1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[start] = 0;
        pq.offer(new Node(start, 0));

        while (!pq.isEmpty()){
            Node now = pq.poll(); // 최소비용 노드 꺼내기
            if (now.cost > dist[now.dest]) continue;
            for (Node nxt : graph[now.dest]){
                if ((nxt.cost + now.cost) < dist[nxt.dest]){
                    dist[nxt.dest] = nxt.cost+now.cost;
                    pq.offer(new Node(nxt.dest, nxt.cost + now.cost));
                }
            }
        }
        return dist; // 배열 만들어서 리턴
    }
}
