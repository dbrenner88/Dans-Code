public class MyName {
    public static void main(String[] args) {

        /*
         * String name = "john";
         * String fName = "dan";
         * String lName = "brenner";
         * String space = " ";
         * String fullName = fName + space + lName;
         * 
         * // printing full name
         * System.out.println(fullName);
         * 
         * int johnNum = 22;
         * int num2;
         * num2 = 11;
         * 
         * // printing john name and numbers
         * System.out.println(name + ' ' + johnNum + ' ' + num2);
         * 
         * // printing addition
         * System.out.println(johnNum + num2);
         * 
         * johnNum = 154;
         * 
         * // printing johns number
         * System.out.println(johnNum);
         * 
         * // final example - cannot change this variable
         * final int fNum = 3;
         * System.out.println(fNum);
         * 
         * // declaring the same type for multiple variables same line
         * int x = 4, y = 5, z = 56;
         * System.out.println(x + y + z);
         * 
         * // different daya type examples
         * byte myNum = 100;
         * System.out.println("This is a byte number example: " + myNum);
         * 
         * short shortNum = 30606;
         * System.out.println("This is a short number example: " + shortNum);
         * 
         * int negInt = -12342342;
         * System.out.println("This is an example of an int " + negInt);
         * 
         * long longNum = 209853052345L;
         * System.out.println("This is an example of a long data type: " + longNum)
         * 
         * float myFloat = 1.235f;
         * System.out.println("This is a float example: " + myFloat);
         * 
         * double myDub = 1.23345345d;
         * System.out.println("This is a double example: " + myDub);
         * 
         * float f1 = 35e3F;
         * double d1 = 12E4d;
         * System.out.println("This is a float e example: " +
         * f1 +
         * ". This is a double E example: " +
         * d1);
         * 
         * // boolean example
         * boolean isJavaFun = true, isFishTasty = false;
         * String isJava = "Is Java Fun? ", isFishGood = "Is fish tasty? ";
         * String period = ".";
         * System.out.print(isJava + isJavaFun);
         * System.out.println(period);
         * System.out.print(isFishGood + isFishTasty);
         * System.out.println(period);
         * 
         * // char example
         * char myGrade = 'A';
         * System.out.println("My Grade is an " + myGrade);
         * 
         * // print out ascci chars
         * char myChar1 = 23, myChar2 = 55, myChar3 = 67;
         * System.out.println(myChar1);
         * System.out.println(myChar2);
         * System.out.println(myChar3);
         */

        // widening example
        int myInt = 9;
        double myDouble = myInt;
        System.out.println(myInt);
        System.out.println(myDouble);

        // narrowing example
        myDouble = 9.78d;
        myInt = (int) myDouble;
        System.out.println(myDouble);
        System.out.println(myInt);

        // operators example
        int x = 100 + 50, y, sum1 = x, sum2 = sum1 + 250, sum3 = sum2 + sum2, sub1 = sum3 - sum1, mult1 = sub1 * x,
                inc1 = ++x, dec1 = --x;
        double div1 = sub1 / 7d, mod1 = inc1 % sub1;
        System.out.println("Operators:");
        System.out.println(sum1);
        System.out.println(sum2);
        System.out.println(sum3);
        System.out.println(sub1);
        System.out.println(mult1);
        System.out.println(div1);
        System.out.println(mod1);
        System.out.println(inc1);
        System.out.println(dec1);

        // assignment operators
        System.out.println("Assignment Opperator Examples:");
        x = 10;
        System.out.println(x);
        x += 5;
        System.out.println(x);
        x -= 3;
        System.out.println(x);
        x *= 13;
        System.out.println(x);
        x /= 8;
        System.out.println(x);
        x %= 4;
        double xDub = (double) x % 4d;
        System.out.println(xDub);
        x &= 8;
        System.out.println(x);
        x |= 3;
        System.out.println(x);
        sum1 ^= 3;
        System.out.println(sum1);
        sum1 >>= 3;
        System.out.println(sum1);
        sum1 <<= 3;
        System.out.println(sum1);

        // Comparison Operators
        x = 5;
        y = 3;
        System.out.println("Comp Operators:");
        System.out.println(x > y);
        System.out.println(x < y);
        System.out.println(x < 5 && x < 10);
        System.out.println(x < 5 || y < 4);
        System.out.println(x < 5 | x < 10);
    }
}