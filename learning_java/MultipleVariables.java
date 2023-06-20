public class MultipleVariables {
    public static void main(String[] args) {

        int x = 10;
        int y = 12;
        int z = 4;
        System.out.println(x + y + z);

        x = y = z = 50;
        System.out.println(x + y + z);

        int xX, yY, zZ;
        xX = yY = zZ = 25;
        System.out.println(xX * yY * zZ);

        String myName, hisName, HerName;
        String space = " ";

        myName = hisName = HerName = "Danny";
        System.out.println(myName + space + hisName + space + HerName);

        double myDouble = 9.78d;
        int myInt = (int) myDouble;
        System.out.println(myInt + myDouble);

        float myD;
        myD = 4.555f;

        String newString = String.valueOf(myDouble);
        System.out.print(newString);
        System.out.println(myD);

    }

}
