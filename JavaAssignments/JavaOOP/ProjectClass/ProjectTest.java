public class ProjectTest{
    public static void main(String[] args){
        Project Project1 = new Project(); 
        Project Project2 = new Project("My Great Project"); 
        Project Project3 = new Project("Project Fun!", "This project is all about fun!! "); 

        System.out.println(Project1.elevatorPitch());
        System.out.println(Project2.elevatorPitch());
        System.out.println(Project3.elevatorPitch());

    }
}