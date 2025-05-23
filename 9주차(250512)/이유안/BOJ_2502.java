import java.util.*;
import java.io.*;
class Main{
    static int d,k;
    static int[] af,bf;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] ip = br.readLine().split(" ");
        d = Integer.parseInt(ip[0]);
        k = Integer.parseInt(ip[1]);

        af = new int[d+1];
        bf = new int[d+1];

        af[1]=1; bf[1]=0; //1일자
        af[2]=0; bf[2]=1; //2일자

        for (int i=3; i<=d; i++){
            af[i] = af[i-1]+af[i-2];
            bf[i] = bf[i-1]+bf[i-2];
        }
        // 완탐으로 가능한 a,b 구하기
        for (int a=1; a<=k/2; a++){
            int res = k-a*af[d];
            if (res%bf[d]!=0) continue;
            if (res/bf[d]<a) continue;

            System.out.println(a);
            System.out.println(res/bf[d]);
            break;
            }
        }
    }
