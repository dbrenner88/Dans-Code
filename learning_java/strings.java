public class strings {
    public static void main(String args[]) {
        String txt = "asdfasdfasrfaweasdfv";
        System.out.println("The length of the string is " + txt.length());

        String newTxt = "Hi Izzy";
        System.out.println(newTxt.toUpperCase());
        System.out.println(newTxt.toLowerCase());

        String txt1 = "Please find Addy in this sentence.";
        System.out.println(txt1.indexOf("Addy"));

        String fName = "Dan";
        String lName = "TheMan";
        System.out.println(fName + " " + lName);
        System.out.println(fName.concat(lName));

        String viking = "We are \"Vikings\" from the north.";
        String ok = "It\'s aallll rightt. We love it. \n It\'s the best.";

        System.out.println(viking);
        System.out.println(ok);
    }

}
