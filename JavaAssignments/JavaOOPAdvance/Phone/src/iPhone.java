
public class iPhone extends Phone implements Ringable {
	
	public iPhone(String versionNumber, int batteryPercentage, String carrier, String ringTone) {
		super(versionNumber, batteryPercentage, carrier, ringTone);
		// TODO Auto-generated constructor stub
	}
	
	@Override
    public String ring() {
        // your code here
		return "iPhone ringtone is: "+this.getRingTone();
    }
    @Override
    public String unlock() {
        // your code here
    	return "Unlocked Via Facial Recognition";
    }
    
	@Override
    public void displayInfo() {
        // your code here         
    	System.out.println("iPhone "+ this.getVersionNumber()+ " from "+ this.getCarrier());
    }
}
