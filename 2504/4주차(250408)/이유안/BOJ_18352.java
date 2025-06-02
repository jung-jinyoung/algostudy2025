/*
n번까지의 도시 m개 도로 거리 1
최단거리 k 인 모든 도시번호 출력
 */

import java.util.*;
import java.io.*;

class Main {
    static int n, m, cnt, s;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 도시개수, 도로 개수, 거리정보, 출발도시 번호
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        cnt = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        // graph: [ [], [], [], [] ]
        ArrayList<ArrayList<Integer>> graph = new ArrayList();
        for (int c = 0; c < (n + 1); c++) {
            graph.add(new ArrayList<>());
        }
//        System.out.println(Arrays.toString(graph));
        for (int i = 0; i < m; i++) {
            String[] inputs = br.readLine().split(" ");
            int x = Integer.parseInt(inputs[0]);
            int y = Integer.parseInt(inputs[1]);
            graph.get(x).add(y);
        }
        // 초기화
        int INF = Integer.MAX_VALUE;
        int[] cities = new int[(n+1)];
        Arrays.fill(cities, INF);
        cities[s] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b) -> a[0] - b[0]);
        pq.offer(new int[]{0, s});//cost, 시작도시
        // 다익스트라
        while (!pq.isEmpty()) {
            int[] now = pq.poll();
            int nowcost = now[0];
            int nowcity = now[1];
//            System.out.println(nowcost+","+nowcity);
            // 이미 지나간 도시 (visit처리)
            if (nowcost > cities[nowcity]) continue;

            for (int nxt : graph.get(nowcity)) {
                if ((nowcost + 1) < cities[nxt]) {
                    cities[nxt] = nowcost + 1;
                    pq.add(new int[]{nowcost + 1, nxt});
                }
            }
        }
//        System.out.println(Arrays.toString(cities));
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<(n+1); i++){
            if (cities[i] == cnt){
                sb.append(i).append('\n');
            }
        }
        if (sb.length()==0){
            System.out.println(-1);
        } else{
            System.out.println(sb);
        }
    }
}