import java.util.*;
import java.io.*;
class Main{
    static int n;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 총 개수
        n = Integer.parseInt(br.readLine());
        String[] ip = br.readLine().split(" ");

        int[] cards = new int[n]; // 카드 배열
        Set<Integer> cs = new HashSet<>(); //카드 셋

        for (int i=0; i<n; i++){
            cards[i] = Integer.parseInt(ip[i]);
            cs.add(cards[i]);
        }
        // card: 점수 map
        Map<Integer, Integer> map = new HashMap<>();
        for (int c: cards){
            map.put(c,0);
        }
        for (int c:cards){
            for (int m = c*2; m<=1000000; m+=c){
                if (cs.contains(m)){
                    // 현재카드c 의 몇배수... 인 m 이 다른 선수 카드인경우
                    // m이 c로 나눠지기때문에 m-1, c+1
                    map.put(c,map.get(c)+1);
                    map.put(m,map.get(m)-1);
                }
            }
        }

//        System.out.println(map.values());
        StringBuilder sb = new StringBuilder();
        for (int c:cards){
            sb.append(map.get(c) + " ");
        }
        System.out.println(sb);





        }
    }
