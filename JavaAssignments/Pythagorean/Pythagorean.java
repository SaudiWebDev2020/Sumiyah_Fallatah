import java.lang.Math;

public class Pythagorean {
    public double calculateHypotenuse(int legA, int legB) {
        // the hypotenuse is the side across from the right angle. 
        // calculate the value of c given legA and legB
        // hypot() does exactly what we want! 

        // cast the given int to double
        double legAd = (double) legA;
        double legBd = (double) legB;


        // long way using pow and sqrt
        double a = Math.pow(legAd , 2);
        double b = Math.pow(legBd , 2); 
        
        double sum = a+b;

        // double res = Math.sqrt(sum);

        //Short Way: 
        double res = Math.hypot(legAd, legBd);

        return res;
    }
}