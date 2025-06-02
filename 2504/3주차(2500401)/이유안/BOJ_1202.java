import java.sql.Array;
import java.sql.SQLOutput;
import java.util.*;
import java.io.*;

class Main {
    static int n,k;
    static int[][] jewels;
    static long[] bags;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        n = Integer.parseInt(inputs[0]);
        k = Integer.parseInt(inputs[1]);

//        [[],[], ...n개  ]
//        ArrayList<int[]> jewels = new ArrayList<>();
        jewels = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            jewels[i][0] = m;
            jewels[i][1] = v;
        }
        bags = new long[(k)];
        for (int i = 0; i < k; i++) {
            bags[i] = Integer.parseInt(br.readLine());
        }
        // 무게 순 정렬 , 보석은 무게순+가치순 정렬
        Arrays.sort(bags);
        Arrays.sort(jewels, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) return Integer.compare(o1[1], o2[1]);
                return Integer.compare(o1[0], o2[0]);
            }
        });

        long answer = 0;
        // 가방에 들어갈 수 있는 모든 보석 체크 해서 넣기
        // 가방 k개, 보석 n개
        int idx = 0; // 보석들 한번만 넣기
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int x=0; x<k; x++){
            long bagW = bags[x];
            while (idx<n && jewels[idx][0]<=bagW ){
                pq.add(-jewels[idx][1]); // 큰거 부터 꺼내야함
                idx++;
            } // 현재 가방에서 가능한 다 넣고
            // 가장 높은 가치 인거 빼서 넣기
            if(!pq.isEmpty()){
                long nowV = pq.poll();
//                System.out.println(nowV);
                answer+=(-nowV);
            }
        }

        System.out.println(answer);


    }
}