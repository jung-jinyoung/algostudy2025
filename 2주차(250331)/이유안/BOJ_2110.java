import java.util.*;
import java.io.*;

class Main{
    static int n,c;
    static long maxDist;

public static void main(String[] args) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine());
    n = Integer.parseInt(st.nextToken());
    c = Integer.parseInt(st.nextToken());

    long [] house = new long[n];
    for (int i=0; i<n; i++){
        long d = Long.parseLong(br.readLine());
        house[i] = d;
    }
    Arrays.sort(house);
//    System.out.println(Arrays.toString(house));
    long left = find(n,house); //최소거리
    long right = (house[n-1]-house[0]); //최대거리

    while (left<=right){
        long mid = (left+right)/2;
        int numConnector = countConnector(house,mid);
        if (numConnector >=c){ // 더 많이 설치했을때
            if (mid>=maxDist){
                maxDist = mid;
            }
            //dist 늘리기
            left = mid+1;
        } else{
            right = mid-1;
        }
    }

    System.out.println(maxDist);
}
    static long find(int n,long[] house){
        long minv = Long.MAX_VALUE;
        for (int i=1; i<n; i++){
            long dist = house[i]-house[i-1];
            if (dist<minv) minv = dist;
        }
        return minv;
    }

    static int countConnector(long[] house,long dist){
        long prev = house[0]; // 맨처음 공유기 설치 위치
        int numC = 1; // 설치된 공유기 개수
        // dist 가 최소의 공유기 설치 거리니까 그거보다 같거나 크면
        // 무조건 공유기 설치해야함
        for (int i=1; i<n; i++){
            if ((house[i]-prev) >=dist){
                prev = house[i];
                numC++;
            }
        }
        return numC;
    }
}
