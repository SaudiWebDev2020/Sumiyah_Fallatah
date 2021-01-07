import java.util.Random;

public class BankAccount {
	static int accountNum = 0;
	static double allTheMoney = 0;

	String accountNumber;
	private double checkingBalance, savingsBalance; 
	
	//Constructor
	public BankAccount() {
		BankAccount.accountNum++;
		this.checkingBalance = 0;
		this.savingsBalance = 0;
		this.accountNumber = BankAccount.generateId();
	}
	
	public static double allMoney() {
		return BankAccount.allTheMoney;
	}
	
	//get user checking account
	public double getCheckingBalance() {
		return this.checkingBalance;
	}
	
	// get saving balance
	public double getSavingBalance() {
		return this.savingsBalance;
	}
	
	//add money to checking
	public void addToCheckingBalance(double value) {
		this.checkingBalance += value;
		BankAccount.allTheMoney += value;
	}
	
	//add money to savings
	public void addToSavingBalance(double value) {
		this.savingsBalance += value;
		BankAccount.allTheMoney += value;
	}
	
	//withdraw money
	public void withdrawFromChecking(double value) {
		if (value < this.checkingBalance) {
			this.checkingBalance -= value;
			System.out.println("Successful withdraw!");
		} else {
			System.out.println("Insufficient funds!");
		}
	}
	
	public void withdrawFromSavings(double value) {
		if (value < this.savingsBalance) {
			this.savingsBalance -= value;
			System.out.println("Successful withdraw!");
		} else {
			System.out.println("Insufficient funds!");
		}
	}
	
	//check account 
	public void checkAccount() {
		System.out.println(String.format("Your account balance in Checking: %.2f \nYour account balance in Savings: %.2f \n", this.checkingBalance, this.savingsBalance));
	}
	
	public static int numberOfAccounts() {
		return BankAccount.accountNum;
	}
	
	//generate id for user... 
	private static String generateId() {
		String newid = "";
		Random r = new Random();
		for(int i = 0; i < 10; i++) {
			newid += r.nextInt(10);
		}
		return newid;
	}
}
