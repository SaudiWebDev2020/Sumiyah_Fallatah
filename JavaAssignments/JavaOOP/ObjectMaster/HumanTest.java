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
        
        Wizard w1 = new Wizard();
        Ninja n1 = new Ninja();
        Samurai s1 = new Samurai();
        Samurai s2 = new Samurai();
        Samurai s3 = new Samurai();
        
        System.out.println("Wizard, Ninja & Samurai:------------------");
        System.out.println("Wizard 1 Status: ");
        w1.displayStatus();
        System.out.println("Ninja 1 Status: ");
        n1.displayStatus();
        System.out.println("Samurai 1 Status: ");
        s1.displayStatus();
        s1.howMany();
        System.out.println("SOME INTERACTIONS: #############");
        //samurai2 kill h1
        s2.deathBlow(h1);
        s2.displayStatus();
        h1.displayStatus();
        s2.meditate();
        s2.howMany();
        s2.displayStatus();

        //Ninja1 and h2
        System.out.println("NINJA AND HUMAN2");
        n1.displayStatus();
        h2.displayStatus();
        n1.steal(h2);
        n1.displayStatus();
        h2.displayStatus();
        n1.runAway();
        n1.runAway();
        
        // Wizard and Samurai3
        System.out.println("Wizard1 and Samurai3::::::::::");
        w1.displayStatus();
        s3.displayStatus();
        System.out.println("Wizard heals h1 : ");
        w1.heal(h1);
        w1.displayStatus();
        h1.displayStatus();

    }
}
