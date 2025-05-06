import java.util.*;
import java.io.*;

class Main {
    static int n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        Map<Integer, Integer> map = new LinkedHashMap<>(); // 학생번호: 추천수

        while (st.hasMoreTokens()) {
            int now = Integer.parseInt(st.nextToken());
            if (map.containsKey(now)) {
                map.put(now, map.get(now) + 1);
                continue;
            }

            if (map.size() < n) {
                map.put(now, 1);
                continue;
            }

            int minVote = Collections.min(map.values());
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                Integer v = entry.getValue();
                if (v==minVote){
                    map.remove(entry.getKey());
                    break;
                }
            }

            map.put(now, 1);
        }

        List<Integer> result = new ArrayList<>(map.keySet());
        Collections.sort(result);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
