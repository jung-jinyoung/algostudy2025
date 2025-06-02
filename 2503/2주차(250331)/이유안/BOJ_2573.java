import java.util.*;
import java.io.*;

class Main{
    static long now = Long.MAX_VALUE;
    static long[] res = new long[3];

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long [] arr = new long[n];
        for (int i=0; i<n; i++){
            arr[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(arr);
        for ( int i=0; i<(n-2); i++){
            long x = arr[i];
            for (int j=i+1; j<(n-1); j++){
                long y = arr[j];

                // 이분탐색
                int left = j+1;
                int right = n-1;
                while (left<=right){
                    int mid = (left+right)/2;
                    long z = arr[mid];
                    // 현재값 추적
                    if (Math.abs(x+y+z) < now){
                        now = Math.abs(x + y + z);
                        res = new long[]{x,y,z};
                    }
                    // y+z 가 -x보다 크면 줄여야하니까 r= mid+1
                    // y+z 가 -x보다 작으면 키워야하니까 l= mid-1
                    if ((y+z)>-x){
                        right = mid-1;
                    }
                    else if ((y+z)<-x){
                        left = mid+1;
                    }
                    else{
                        res = new long[]{x,y,z};
                        Arrays.sort(res);
                        for (long r :res){
                            System.out.print(r);
                            System.out.print(" ");
                        }
                        return;
                    }

                }

            }
        }
        Arrays.sort(res);
        for (long r :res){
            System.out.print(r);
            System.out.print(" ");
        }
    }
}