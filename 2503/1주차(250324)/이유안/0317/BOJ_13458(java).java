/*
범위확인: 숫자 크면 long 으로 써줘야함
 */


import java.util.*;
import java.io.*;

class Main{

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long n = Integer.parseInt(br.readLine());
        long[] stds = Arrays.stream(br.readLine().split(" "))
                .mapToLong(Integer::parseInt)
                .toArray();

        StringTokenizer st = new StringTokenizer(br.readLine());
        long t1 = Integer.parseInt(st.nextToken());
        long t2 = Integer.parseInt(st.nextToken());

        long total = n;

        for (int i=0; i<n; i++){
            long number = (stds[i]-t1);
            if ( number>0){
                total += (number / t2);
                if (number%t2>0){
                    total++;
                }

//                long k = (number/t2);
//                long d = (number%t2);
//                if (d>0) {
//                    total+=(k+1);
//                }else{
//                    total+=k;
//                }
            }

        }

            System.out.println(total);
    }
}