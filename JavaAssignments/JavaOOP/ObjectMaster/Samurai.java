public class Samurai extends Human {
    private static int count = 0;
    public Samurai(){
        super.health=200;
        Samurai.count+=1;
    }
    
    public void deathBlow(Human human){
        human.health=0;
        this.health= this.health / 2;
    }

    public void meditate(){
        this.health=200;
    }

    public void howMany(){
        System.out.println("The amount of Samurais: "+ Samurai.count);
    }
}
