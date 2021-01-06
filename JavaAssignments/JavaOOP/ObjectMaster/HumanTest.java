public class HumanTest {
    public static void main (String[] args){
        Human h1 = new Human();
        Human h2 = new Human();

        System.out.println("Human 1 Status: ");
        h1.displayStatus();
        System.out.println("Human 2 Status: ");
        h2.displayStatus();
        
        h1.attack(h2);
        System.out.println("AFTER ATTACK:------------------");
        System.out.println("Human 1 Status: ");
        h1.displayStatus();
        System.out.println("Human 2 Status: ");
        h2.displayStatus();

    }
}
