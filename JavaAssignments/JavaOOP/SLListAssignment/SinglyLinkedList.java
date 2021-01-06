public class SinglyLinkedList {
    public Node head;
    public SinglyLinkedList() {
        // your code here
        this.head = null;
    }
    // SLL methods go here. As a starter, we will show you how to add a node to the list.
    public void add(int value) {
        Node newNode = new Node(value);
        if(head == null) {
            head = newNode;
        } else {
            Node runner = head;
            while(runner.next != null) {
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }   

    public String find(int value) {
        Node runner = this.head;
        while(runner != null) {
            if(runner.value == value)
                return "Found the value " + value;
            runner = runner.next;
        }
        return "Value "+ value +" is not in list";

    }
    
    public Integer remove(){
        Integer removedValue;
        Node runner = head;
        if (head == null){
            return null;
        } 
        
        if (head.next == null){
            removedValue = head.value;
            head = null; 
            return removedValue;
        }

        while(runner.next.next != null) {
            runner = runner.next;
        }
        removedValue = runner.next.value;
        runner.next = null;
        return removedValue;
    }

    public void printValues(){
        if (head == null){
            System.out.println("Empty List!");
        }
        Node runner = this.head;
        while(runner.next != null) {
            System.out.println("$$$$$$$$$$$$$$$$");
            String s = String.format("Node Value: %s :: Nexint Value: %s", runner.value, runner.next.value);
            System.out.println(s);
            runner = runner.next;
        }
        System.out.println("$$$$$$$$$$$$$$$$");
        String s = String.format("Node Value: %s :: Nexint Value: null", runner.value);
        System.out.println(s);
    }
}
