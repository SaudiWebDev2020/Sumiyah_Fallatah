
public class BankAccountTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BankAccount ba = new BankAccount();
		ba.checkAccount();
		ba.addToSavingBalance(100.42);
		ba.addToCheckingBalance(3538.73);
		ba.checkAccount();
		
		System.out.println("all the money: " + ba.allMoney());
		
		ba.withdrawFromSavings(200);
		
		ba.withdrawFromChecking(200.134);
		ba.checkAccount();
		
	}

}
