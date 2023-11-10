> Description
> We found this weird message being passed around on the servers, we think we have a working decryption scheme.
> Download the message here.
> Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
> Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})
>
> > message : 165 248 94 346 299 73 198 221 313 137 205 87 336 110 186 69 223 213 216 216 177 138

```
#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    int arr[22];
    for(int i = 0; i < 22; i++) {
        cin >> arr[i];
        arr[i] = arr[i] % 37;
        if(arr[i] >= 0 && arr[i] < 26) arr[i] += 65;
        else if(arr[i] > 25 && arr[i] < 36) arr[i] += 22;
        else if(arr[i] == 36) arr[i] = 95;
        printf("%c", arr[i]);
    }
    return 0;
}
/*
character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
*/
```

`picoCTF{R0UND_N_R0UND_B6B25531}`
