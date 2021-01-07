
public class PhoneTester {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Galaxy s9 = new Galaxy("S9", 99, "Mobily", "Ring Ring Rang!!");
		iPhone proMax = new iPhone ("12 Pro Max", 100, "stc", "Zinng");
		
		s9.displayInfo();
		System.out.println(s9.ring());
		System.out.println(s9.unlock());
		
		proMax.displayInfo();
		System.out.println(proMax.ring());
		System.out.println(proMax.unlock());
		
	}

}
