public class Human {
    int strength, stealth, intelligence, health;
    public Human(){
        this.health=100;
        this.stealth=3;
        this.intelligence=3;
        this.strength=3;
    }

    public void attack(Human human){
        human.health-=this.strength;
    }

    public void displayStatus(){
        System.out.println("Health "+ this.health);
        System.out.println("Stealth " + this.stealth);
        System.out.println("Strength " + this.strength);
        System.out.println("Intelligence " +this.intelligence);
        System.out.println("******************");
    }
    
}
