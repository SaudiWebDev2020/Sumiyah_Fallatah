public class Mammal {
    int energyLevel;

    public Mammal(){
        this.energyLevel=100;
    }
    public int displayEnergy(){
        System.out.println("Energy Level is: "+ this.energyLevel+"/100");
        return this.energyLevel;
    }
}
