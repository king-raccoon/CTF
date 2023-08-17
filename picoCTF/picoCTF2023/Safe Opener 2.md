> What can you do with this file?
> I forgot the key to my safe but this file is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

```
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Base64;

public class SafeOpener {
  public static void main(String[] args) throws IOException {
    BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
    Base64.Encoder encoder = Base64.getEncoder();
    String encodedkey = "";
    String key = "";
    int i = 0;
    while (i < 3) {
      System.out.print("Enter password for the safe: ");
      key = keyboard.readLine();
      encodedkey = encoder.encodeToString(key.getBytes());
      System.out.println(encodedkey);
      boolean isOpen = openSafe(encodedkey);
      if (!isOpen) {
        System.out.println("You have  " + (2 - i) + " attempt(s) left");
        i++;
      }
    }
  }

  public static boolean openSafe(String password) {
    String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_198203f7}";
    if (password.equals(encodedkey)) {
      System.out.println("Sesame open");
      return true;
    }
    System.out.println("Password is incorrect\n");
    return false;
  }
}
```

`picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_198203f7}`
