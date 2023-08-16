> Decrypt this message.
>
> > picoCTF{ynkooejcpdanqxeykjrbdofgkq}

ascii code
a~z → 97~122

```
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string str = "ynkooejcpdanqxeykjrbdofgkq";
    int len = str.size();
    for(int i = 1; i < 26; i++){
        for(int j = 0; j < len; j++){
            printf("%c", ((str[j] + i) -97) % 26 + 97);
        }
        cout << endl;
    }
    return 0;
}
```

```
//output
zolppfkdqeboryfzlkscepghlr
apmqqglerfcpszgamltdfqhims
bqnrrhmfsgdqtahbnmuegrijnt
crossingtherubiconvfhsjkou
dspttjohuifsvcjdpowgitklpv
etquukpivjgtwdkeqpxhjulmqw
furvvlqjwkhuxelfrqyikvmnrx
gvswwmrkxlivyfmgsrzjlwnosy
hwtxxnslymjwzgnhtsakmxoptz
ixuyyotmznkxahoiutblnypqua
jyvzzpunaolybipjvucmozqrvb
kzwaaqvobpmzcjqkwvdnparswc
laxbbrwpcqnadkrlxweoqbstxd
mbyccsxqdrobelsmyxfprctuye
nczddtyrespcfmtnzygqsduvzf
odaeeuzsftqdgnuoazhrtevwag
pebffvatgurehovpbaisufwxbh
qfcggwbuhvsfipwqcbjtvgxyci
rgdhhxcviwtgjqxrdckuwhyzdj
sheiiydwjxuhkrysedlvxizaek
tifjjzexkyvilsztfemwyjabfl
ujgkkafylzwjmtaugfnxzkbcgm
vkhllbgzmaxknubvhgoyalcdhn
wlimmchanbylovcwihpzbmdeio
xmjnndiboczmpwdxjiqacnefjp
```

`picoCTF{crossingtherubiconvfhsjkou}`
