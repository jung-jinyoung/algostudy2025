import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        Queue<Long> q1 = new ArrayDeque<>();
        Queue<Long> q2 = new ArrayDeque<>();
        long s1=0,s2 = 0;
        for (int q:queue1){
            s1+=q;
            q1.add((long)q);
        }
        for (int q:queue2){
            s2+=q;
            q2.add((long)q);
        }
        long h = (s1+s2)/2;
        int cnt = 0; 
        int maxT = q1.size() *3; 
        while (cnt<maxT){
            if (s1==h){
                return cnt;
            }
            else if (s1<h){
                long l = q2.poll();
                q1.add(l);
                s1+=l;
            }
            else if (s1>h){
                long l = q1.poll();
                q2.add(l);
                s1-=l;
            }
            cnt++;
        }
        
        return -1;
    }
}