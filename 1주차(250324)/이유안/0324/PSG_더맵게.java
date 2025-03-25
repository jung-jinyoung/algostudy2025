import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int n : scoville){
            pq.add(n);
        }
        
        int cnt = 0;
        int j = 0;
        
        while (pq.size()>1){
            int x = pq.poll();
            if (x>=K) return cnt;
            
            int y = pq.poll();
            pq.add(x+y*2);
            
            cnt++;
        }
        
        return pq.peek() >=K ? cnt : -1;
    }
}