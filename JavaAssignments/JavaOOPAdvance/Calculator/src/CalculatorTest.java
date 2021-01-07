
public class CalculatorTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Calculator c = new Calculator();
		
		c.setOperandOne(10.5);
		c.setOperation("+");
		c.setOperandTwo(5.2);
		c.performOperation();
		System.out.println("Result of "+ c.getOperandOne()+" "+ c.getOperation() + " " + c.getOperandTwo() +" = "+c.getResult());
	
		
		c.setOperandOne(50.2);
		c.setOperation("-");
		c.setOperandTwo(10.2);
		c.performOperation();
		System.out.println("Result of "+ c.getOperandOne()+" "+ c.getOperation() + " " + c.getOperandTwo() +" = "+c.getResult());
	
		c.setOperandOne(10);
		c.setOperation("/");
		c.setOperandTwo(2);
		c.performOperation();
		System.out.println("Result of "+ c.getOperandOne()+" "+ c.getOperation() + " " + c.getOperandTwo() +" = "+c.getResult());
	
		c.setOperandOne(6);
		c.setOperation("%");
		c.setOperandTwo(5);
		c.performOperation();
		System.out.println("Result of "+ c.getOperandOne()+" "+ c.getOperation() + " " + c.getOperandTwo() +" = "+c.getResult());
	
		c.setOperandOne(10);
		c.setOperation("*");
		c.setOperandTwo(30.794);
		c.performOperation();
		System.out.println("Result of "+ c.getOperandOne()+" "+ c.getOperation() + " " + c.getOperandTwo() +" = "+c.getResult());
	
	}

}
