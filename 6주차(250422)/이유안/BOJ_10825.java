import java.util.*;
import java.io.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // n명
        // 이름, 국,영,수
        // 국어 내림차순, 영 오름차순, 수 내림차순
        // 이름 오름차순
        // 이름 정렬
        int n = Integer.parseInt(br.readLine());
        List<String[]> arr = new ArrayList<>();
        for (int i=0; i<n; i++){
            String[] inputs = br.readLine().split(" ");
            arr.add(inputs);
        }

        Collections.sort(arr,new Comparator<String[]>(){
            @Override
            public int compare(String[] a, String[] b){
                int x1 = Integer.parseInt(a[1]);
                int x2 = Integer.parseInt(b[1]);
                int y1 = Integer.parseInt(a[2]);
                int y2 = Integer.parseInt(b[2]);
                int z1 = Integer.parseInt(a[3]);
                int z2 = Integer.parseInt(b[3]);
                // 국어 내림차순, 영 오름차순, 수 내림차순
                // 이름 오름차순
                if (x1!=x2) return x2-x1;
                else if (y1!=y2) return y1-y2;
                else if (z1!=z2) return z2-z1;
                return a[0].compareTo(b[0]);
            }

        });

        for (String[] ar:arr){
            System.out.println(ar[0]);
        }
    }
}
