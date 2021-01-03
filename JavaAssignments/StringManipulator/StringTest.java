public class StringTest{
    public static void main(String[] args){
        StringManipulator SM = new StringManipulator();

        //Trim and Concat
        String str = SM.trimAndConcat("    Hello     ","     World    ");
        // System.out.println("Trim & Concat: \n" + str);

        //Index or null -Char
        char letter = 'o';
        Integer a = SM.getIndexOrNull("Coding", letter);
        Integer b = SM.getIndexOrNull("Hello World", letter);
        Integer c = SM.getIndexOrNull("Hi", letter);
        // System.out.println(a); // 1
        // System.out.println(b); // 4
        // System.out.println(c); // null

        // Index or null - substring
        String word = "Hello";
        String subString = "llo";
        String notSubString = "world";
        Integer d = SM.getIndexOrNull(word, subString);
        Integer e = SM.getIndexOrNull(word, notSubString);
        // System.out.println(d); // 2
        // System.out.println(e); // null

        String myWord = SM.concatSubstring("Hello", 1, 2, "world");
        System.out.println(myWord); // eworld
    }
}