public class Gorilla extends Mammal{
    public Gorilla(){
        super();
    }
    public void throwSomething(){
        System.out.println("The Gorilla has thrown somthing at a human!!!");
        this.energyLevel-=5;
    }

    public void eatBananas(){
        System.out.println("Yummy I ate a really good Banana<3!");
        this.energyLevel+=10;
    }

    public void climb(){
        System.out.println("I climbed a Tree, the view is great!!!");
        this.energyLevel-=10;
    }
}
