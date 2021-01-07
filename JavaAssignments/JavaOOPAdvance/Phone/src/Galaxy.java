
public class Galaxy extends Phone implements Ringable {

	public Galaxy(String versionNumber, int batteryPercentage, String carrier, String ringTone) {
		super(versionNumber, batteryPercentage, carrier, ringTone);
		// TODO Auto-generated constructor stub
	}

	@Override
    public String ring() {
        // your code here
		return "Galaxy ringtone is : "+this.getRingTone();
    }
    @Override
    public String unlock() {
        // your code here
    	return "Unlocked Via Finger Print!";
    }
    @Override
    public void displayInfo() {
        // your code here     
    	System.out.println("Galaxy "+ this.getVersionNumber()+ " from "+ this.getCarrier());
    }

}
