public class FizzBuzzTest{
    public static void main (String[] args){
        FizzBuzz FB = new FizzBuzz();
        System.out.println(FB.isFizzBuzz(21)); //3 - fizz
        System.out.println(FB.isFizzBuzz(30)); //3&5 - fizzbuzz
        System.out.println(FB.isFizzBuzz(55)); //5 - buzz
        System.out.println(FB.isFizzBuzz(7));
    }
}