> Can you get the flag?
> Reverse engineer this Java program

```
//Java program
import java.util.Scanner;

public class KeygenMe {
  public static void main(String[] paramArrayOfString) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter key:");
    String str = scanner.nextLine();
    if (str.length() != 34) {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(33) != '}') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(32) != 'd') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(31) != '0') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(30) != 'a') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(29) != '1') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(28) != 'e') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(27) != 'f') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(26) != 'b') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(25) != '2') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(24) != '_') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(23) != 'd') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(22) != '3') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(21) != 'r') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(20) != '1') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(19) != 'u') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(18) != 'q') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(17) != '3') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(16) != 'r') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(15) != '_') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(14) != 'g') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(13) != 'n') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(12) != '1') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(11) != 'l') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(10) != '0') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(9) != '0') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(8) != '7') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(7) != '{') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(6) != 'F') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(5) != 'T') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(4) != 'C') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(3) != 'o') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(2) != 'c') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(1) != 'i') {
      System.out.println("Invalid key");
      return;
    }
    if (str.charAt(0) != 'p') {
      System.out.println("Invalid key");
      return;
    }
    System.out.println("Valid key");
  }
}
```

`flag : picoCTF{700l1ng_r3qu1r3d_2bfe1a0d}`
