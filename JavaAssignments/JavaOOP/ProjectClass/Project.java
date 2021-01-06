class Project{
    private String name;
    private String description;
    private String nameDefault = "DefaultName";
    private String descriptionDefault ="Default Project";


    public Project() {
        name = nameDefault;
        description = descriptionDefault;
    }

    public Project(String name) {
        this.name = name;
        this.description=descriptionDefault;
    }
    
    public Project(String name, String description) {
        this.name = name;
        this.description = description;

    }

    public String elevatorPitch(){
        return name + " : "+ description;

    }
    public void setName(String projectName){
        this.name = projectName;
    }

    public void setDesc (String projectDesc){
        description = projectDesc;
    }

    public String getName(){
        return name;
    }

    public String getDescription(){
        return description;
    }
}