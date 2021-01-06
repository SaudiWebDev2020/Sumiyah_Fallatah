public class Ninja extends Human {
    public Ninja(){
        super.stealth = 10;
    }

    public void steal(Human human){
        int amountToSteal = this.stealth;
        human.health-= amountToSteal;
        this.stealth+= amountToSteal;
    }
    
    public void runAway(){
        this.health-=10;
    }
}
