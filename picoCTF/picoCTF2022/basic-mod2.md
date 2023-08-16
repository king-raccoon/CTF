> Description
> A new modular challenge!
> Download the message here.
> Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
> Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
>
> > message : 268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131

```
#include <iostream>
#include <stdio.h>
using namespace std;

int modInverse(int A, int M)
{
    for (int X = 1; X < M; X++){
        if (((A % M) * (X % M)) % M == 1)
            return X;
    }
    return 0;
}

int main()
{
    int arr[23], result[23];
    for(int i = 0; i < 23; i++) {
        cin >> arr[i];
        arr[i] %= 41;
    }
    for(int i = 0; i < 23; i++){
        result[i] = modInverse(arr[i], 41);
        if(result[i] >= 1 && result[i] <= 26) result[i] += 96;
        else if(result[i] >= 27 && result[i] <= 36) result[i] += 21;
        else if(result[i] == 37) result[i] = 95;
        printf("%c", result[i]);
    }
    return 0;
}
/*
1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.
104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377
*/
```

`picoCTF{1nv3r53ly_h4rd_8a05d939}`
