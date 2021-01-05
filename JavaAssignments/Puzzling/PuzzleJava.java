import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.Arrays;

public class PuzzleJava {
    public static void main (String[] args){
        int[] nums = {3,5,1,2,7,9,8,13,25,32};
        ArrayPuzzle(nums);
        System.out.println(Arrays.toString(nums));
        
        ArrayList<String> names = new ArrayList<String>();
        names.add("Nancy");
        names.add("Jinchi");
        names.add("Fujibayashi");
        names.add("Momochi");
        names.add("Ishikawa");
        
        
        System.out.println(puzzleName(names));
        
        ArrayList<Character> letters = new ArrayList<Character>(); 
        Character[] alphabets = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
        
        for (Character c : alphabets){
            letters.add(c);
        }
        
        // System.out.println(letters);
        System.out.println(puzzleAlpabet(letters));
        
        //10 random from 55-100
        System.out.println(Arrays.toString(RandomIntArray(55,100)));
    }
    

    public static ArrayList<Character> puzzleAlpabet (ArrayList<Character> charArr){
        Collections.shuffle(charArr);
        System.out.println(String.format("%s is first", charArr.get(0)));
		System.out.println(String.format("%s is last", charArr.get(25)));
        if (isVowel(charArr.get(0))){
            System.out.println("The first letter is a vowel!");
        }
        return charArr;
    }

    public static boolean isVowel (char c){
        return (
            c == 'a' || 
            c == 'i' || 
            c == 'o' || 
            c == 'u' || 
            c == 'e' 
        );
    }
    
    public static ArrayList<String> puzzleName (ArrayList<String> strArr){
        Collections.shuffle(strArr);
        System.out.println(strArr);     
        ArrayList<String> namesLong = new ArrayList<String>();
        for(String name : strArr){
            if(name.length() > 5){
                namesLong.add(name);
            }
        }
        return namesLong;
    }

    public static int[] RandomIntArray(int lowerBound, int upperBound) {
        int[] arr = new int[10];
        int offset = upperBound - lowerBound;
        Random r = new Random();
        for (int i = 0; i < arr.length; i++) {
            arr[i] = r.nextInt(offset) + lowerBound;
        }
        Arrays.sort(arr);
        System.out.printf("Min Value: %d, Max Value: %d\n", arr[0], arr[arr.length-1]);
        return arr; 
    }

    public static int[] ArrayPuzzle(int[] numbers) {
        PuzzleJava PJ = new PuzzleJava();
        System.out.println(PJ.printSum(numbers) + " is sum of numbers");
		int[] newArr = new int [PJ.greaterThanY(numbers, 10)];
		return newArr;
	}

    public int greaterThanY(int[] arr, int y){
        int counter = 0; 
        for(int i = 0; i < arr.length; i++){
            if(arr[i]> y){
                counter++;
                System.out.println(arr[i]);
            }
        }
        return counter;
    }

    public int printSum( int[] arr){
        int sum = 0 ;
        for(int i=0; i <arr.length ; i++){
            sum += arr[i];
        }
        return sum;
    }
}