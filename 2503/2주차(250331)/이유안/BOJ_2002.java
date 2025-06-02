import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int res = 0;
        Deque<String> inOrder = new ArrayDeque<>();
        Deque<String> outOrder = new ArrayDeque<>();

        for (int i=0; i<n; i++){
            inOrder.offer(br.readLine());
        }
        for (int i=0; i<n; i++){
            outOrder.offer(br.readLine());
        }

        while (!outOrder.isEmpty()){
            String now = outOrder.poll();
            Deque<String> waiting = new ArrayDeque<>();
            boolean check = false;
            while(!inOrder.isEmpty()){
                String inCar = inOrder.poll();
                if (inCar.equals(now)){
                    break;
                } else{
                    check = true;
                    waiting.add(inCar);
                }
            }
            // inOrder 갱신해주기
            while (!inOrder.isEmpty()){
                waiting.add(inOrder.poll());
            }
            inOrder = waiting;

            if (check) res++;
        }

        System.out.println(res);

    }
}