public class StringManipulator{

    public String trimAndConcat(String str1, String str2){
        String str3 = str1.trim().concat(str2.trim()); 
        return str3;
    }

    public Integer getIndexOrNull(String S1, char C1){
        return S1.indexOf(C1);
    }

    public Integer getIndexOrNull(String str1, String subStr){
        return str1.indexOf(subStr);
    }

    public String concatSubstring(String str1, int i, int j, String str2){
        return str1.substring(i,j).concat(str2);
    }
}