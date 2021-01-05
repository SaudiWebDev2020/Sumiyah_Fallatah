

public class BasicJava {
    public static void main (String[] args){
        BasicJava BJ = new BasicJava();
        // System.out.println("1 to 255");
        // BJ.oneTo255();

        // System.out.println("1 to 255 - ODD -");
        // BJ.oddIn255();
        
        // System.out.println("Sum 0 to 255!");
        // BJ.printSum();
        
        // System.out.println("Iterate through array");
        int[] myArr = {1,3,5,7,9,13};
        // BJ.iterateArr(myArr);
        
        // System.out.println("max of array is : "+BJ.findMax(myArr));
        
        // Greater than Y 
        // System.out.println("values greater than 5 are : "+BJ.greaterThanY(myArr, 5));
        // System.out.println("values greater than 1 are : "+BJ.greaterThanY(myArr, 1));
        
        int[] myArr2 = {-3,2,-7,12,-9};
        // System.out.println(BJ.sqrValues(myArr2));
        
        // eliminate negatives
        // BJ.noNegatives(myArr2);

        // min, mix, avg
        // BJ.MMandA(myArr);
        // BJ.MMandA(myArr2);

        //shift
        BJ.shift(myArr);

    }

    public void shift(int[] arr){

        for(int i = 0; i< arr.length-1; i++){
            arr[i] = arr[i+1];
            System.out.println(arr[i]);
        }

        arr[arr.length-1] =0;
        System.out.println(arr[arr.length-1]);

    }

    public void MMandA(int[] arr){
        int[] result = new int[3];
        //max 
        BasicJava bj = new BasicJava();
        result[0] = bj.findMax(arr);
        System.out.printf("Max: %d\n",result[0]);
        
        int sum =0, min = arr[0];
        for (int i = 0; i < arr.length; i++){
            if(arr[i]< min){
                min = arr[i];
            }
            sum = sum+arr[i];
        }
        result[1]=min;
        result[2] = sum/arr.length;

        System.out.printf("Min: %d\n",result[1]);
        System.out.printf("Avg: %d\n",result[2]);

    }

    public void noNegatives(int[] arr){
        for (int i = 0 ; i < arr.length; i ++ ){
            if(arr[i]< 0){
                arr[i] = 0;
            }
            System.out.println(arr[i]);
        }
    }

    public int[] sqrValues (int[] arr){
        for(int i = 0; i < arr.length; i++){
            arr[i] = arr[i]*arr[i];
            System.out.println(arr[i]);
        }
        return arr;
    }

    public int greaterThanY(int[] arr, int y){
        int counter = 0; 
        for(int i = 0; i < arr.length; i++){
            if(arr[i]> y){
                counter++;
            }
        }
        return counter;
    }

    public int findMax (int[] arr){
        int max = arr[0];
        for (int i = 1 ; i <arr.length; i++){
            if (arr[i]>max){
                max = arr[i];
            }
        }
        return max;
    }

    public void oneTo255 () {
        for(int i=1; i <=255; i++){
            System.out.println(i);
        }
    }

    public void oddIn255 () {
        for(int i=1; i <=255; i++){
            if(i%2 ==1){
                System.out.println(i);
            }
        }
    }

    public void printSum(){
        int sum = 0 ;
        for(int i=0; i <=255; i++){
            sum += i;
            System.out.printf("New number: %d  Sum: %d \n", i, sum);
        }
    }

    public void iterateArr( int[] arr ){
        for ( int i = 0; i <arr.length; i ++ ){
            System.out.println(arr[i]);
        }
    }

}