
public class Calculator {

	private double operandOne;
	private String operation;
	private double operandTwo;
	private double result;
	public double getOperandOne() {
		return operandOne;
	}
	public void setOperandOne(double operandOne) {
		this.operandOne = operandOne;
	}
	public String getOperation() {
		return operation;
	}
	public void setOperation(String operation) {
		this.operation = operation;
	}
	public double getOperandTwo() {
		return operandTwo;
	}
	public void setOperandTwo(double operandTwo) {
		this.operandTwo = operandTwo;
	}
	public double getResult() {
		return result;
	}
	public void setResult(double result) {
		this.result = result;
	}
	
	public void performOperation() {
		if (this.getOperation() == "+") {
			this.setResult( getOperandOne() + getOperandTwo());
		} else if (this.getOperation() == "-") {
			this.setResult( getOperandOne() - getOperandTwo());
		} else if (this.getOperation() == "/") {
			this.setResult( getOperandOne() / getOperandTwo());
		} else if (this.getOperation() == "*") {
			this.setResult( getOperandOne() * getOperandTwo());
		} else if (this.getOperation() == "%") {
			this.setResult( getOperandOne() % getOperandTwo());
		}
	}
	

}
