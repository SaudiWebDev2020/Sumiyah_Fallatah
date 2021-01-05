import java.util.HashMap;
import java.util.Set;

public class HashMapTracks{
    public static void main(String[] args){
        HashMap<String, String> trackList = new HashMap<String, String>();
        trackList.put("Snowman", "I want you to know that I'm never leaving, cus I'm Mrs. Snow till death will be freezing");
        trackList.put("If the World Was Ending", "I was distracted And in traffic I didn't feel it When the earthquake happened");
        trackList.put("Someone You Loved", "Now the day bleeds, into nightfall, and you're not here to get me throught it all");
        trackList.put("September Song", "You were my September song Summer lasted too long Time moves so slowly When you're only fifteen");

        //print one: 
        String title = trackList.get("September Song");
        System.out.println("Song lyrics: " + title);

        System.out.println("--------------------");
        //print all:
        Set<String> keys = trackList.keySet();
        for(String Track : keys) {
            System.out.println(Track + " : "+ trackList.get(Track));
            // System.out.println(trackList.get(Track));    
        }
    }
}