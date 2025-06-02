import java.util.*;
import java.io.*;

class Main{
    static int k;
    static long n;
    // k개 랜선, n개로 만들기
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");
        k = Integer.parseInt(inputs[0]);
        n = Long.parseLong(inputs[1]);
        long[] lines = new long[k];
        for (int i=0; i<k; i++){
            lines[i] = Long.parseLong(br.readLine());
        }
        Arrays.sort(lines);
        // left, right, mid해서 랜선 길이 정하기
        long left = 1;
        long right = lines[k-1];
        long res = 0;
        while (left<=right){
            long mid = (left+right)/2;
            // mid 기준으로 자를떄 몇개 가능한지 체크
            long cnt = cut(lines, mid);
            if (cnt>= n){
                if (mid>=res){
                    res = mid;
                }
                left = mid+1;
            }else{
                right = mid-1;
            }

        }
        System.out.println(res);
    }

    private static long cut(long[] lines, long mid) {
        long total = 0;
        if (mid!=0){
            for (long line:lines){
                total += (line / mid);
            }
        }else{
            total = lines.length;
        }
        return total;
    }


}