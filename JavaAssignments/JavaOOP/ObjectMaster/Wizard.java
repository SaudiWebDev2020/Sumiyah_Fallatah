public class Wizard extends Human {
    public Wizard(){
        super.health = 50;
        super.intelligence = 8;
    }

    public void heal(Human human){
        human.health+= (this.intelligence * 3);
    }

    public void fireball(Human human){
        human.health-= (this.intelligence * 3);
    }

}
