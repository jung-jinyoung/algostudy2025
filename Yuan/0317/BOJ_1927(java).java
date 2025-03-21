/*
최소힙 : priorityQueue<> pq
pq.add() 와 pq.poll()

*/
import java.util.*;
import java.io.*;

class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for ( int i=0; i<n; i++){
            int number = Integer.parseInt(br.readLine().trim());
//            number 가 0일때
            if (number == 0){
//                pq 가 비어있으면 0 프린트 / 안비어있으면 가장작은 수 프린트
                if (pq.isEmpty()) {
                    sb.append("0\n");
//                    System.out.println(0);
                } else{
//                    int x = pq.poll();
                    sb.append(pq.poll()).append("\n");
//                    System.out.println(x);
                }
            }
            else{
                pq.add(number);
            }
        }
        System.out.print(sb);
    }

}