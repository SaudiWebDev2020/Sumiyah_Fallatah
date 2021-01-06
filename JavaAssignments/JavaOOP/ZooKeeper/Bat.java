public class Bat extends Mammal {
    public Bat(){
        super.energyLevel=300;
    }

    public void fly(){
        System.out.println("WOOOOOSH - the bat has flown!! @__@");
        this.energyLevel-=50;
    }

    public void eatHumans(){
        System.out.println("MUnch mUNch YummYyY HumAanS");
        this.energyLevel+=25;
    }

    public void attackTown(){
        System.out.println("Lets burn this TOWWWWNNN");
        this.energyLevel-=100;
    }
}
