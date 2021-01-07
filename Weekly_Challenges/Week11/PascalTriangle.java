import java.util.ArrayList;

public class PascalTriangle {
    public static void main (String[] args){
        int n = 6;
        printTriangle(n);
    }

    public static int makeTriangle(int n, int k){
        int result = 1; 
        if (k > n-k ){
            k=n-k;
        }

        for (int i=0; i < k ; i++){
            result*= (n-i);
            result/=(i+1);

        }
        return result;
    }

    public static void printTriangle(int n){
        ArrayList<Integer> list = new ArrayList<>();
        for (int line =0; line < n ; line ++){
            for (int i = 0 ; i <= line; i++){
                list.add(makeTriangle(line, i));
            }
            System.out.println(list);
            list.clear();
        }
    }
}
