> Name이 CodeEngn일때 Serial은 28BF522F-A5BE61D1-XXXXXXXX 이다.
> <br>XXXXXXXX 를 구하시오

![1](https://github.com/king-raccoon/Yoom/assets/78426205/621f9e15-2f2d-4517-89bb-801c137adb57)
눌러도 별 반응이 없다

![2](https://github.com/king-raccoon/Yoom/assets/78426205/782e5b78-1eb2-4e83-b728-92988f0cb3ec)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/d296bb81-0803-44d2-8def-841acc442a8a)

```
// Decompiled with JetBrains decompiler
// Type: WindowsFormsApplication2.Program
// Assembly: SpareTimeKeygenme, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
// MVID: 851BF7D6-F2A7-4ABE-AE59-9D2008D077E2
// Assembly location: C:\Users\user\Downloads\07.exe

using System;
using System.Windows.Forms;

namespace WindowsFormsApplication2
{
  internal static class Program
  {
    [STAThread]
    private static void Main()
    {
      Application.EnableVisualStyles();
      Application.SetCompatibleTextRenderingDefault(false);
      Application.Run((Form) new Form1());
    }
  }
}
```

main 함수를 찾아서 확인하면 Form1을 실행함을 알 수 있다

InitializeComponent 함수는 처음에 실행되는 메세지 박스와 관련되어있고 그 밑이 시리얼 값과 관련있다

textBox1은 5 이상인데 InitializeComponent에서 HMX0101을 넣은 것으로 봐 Name인 것 같다

textBox2는 26글자이므로 시리얼 값일것이다

str1에 시리얼 값 앞 8글자를 넣고, str2에 시리얼[9 : 17], str3에는 시리얼[18 : 26]을 넣는다

unit32_i는 stri를 16진수로 변환한 값을 저장

unit32_1과 2를 yreee[]에 넣었다

fsfsdf = uni32_3 ^ hashCode(== uni32_1)

yreee[3] == num1== unit32_2

vxzzz 함수 분석 → 인자 : yreee, ewrrr, 0x8FFE2225, fsfsdf

0x8FFE 2225 ^= fsfsd

num1 = 0x8FFE2225 % 0x39 -1 = 0x286B43E

num2 = unit32_1 =str1

nim3 = unit32_2 = str2

num4 = num1 = 0x286B43E

num5 = 0x8FFE2225 <<(97 ^ num1 + 68)

num6 = num4 / 10

num7 = num2 << (num4 / 8)

num8 = num2 >> 3 + num6

num9 = num4 / 4 + 3

num10 = num9

ewrrr = ewrrr[(num5 >> num9) % 4]

num11 = num5 + ewrrr

num12 = nun3 - (((num7 ^ num8) + num2 ^ num11) - num1)

num5 -= 0x8FFE2225

num3 = num12 - num1 ⇒ nun3 - (((num7 ^ num8) + num2 ^ num11) - num1) - num1

근데 이거 그냥 00000000부터 ffffffff 중 맞는거 찾으면 안되나

분석하다가 눈 빠질듯

```
for (int index = 18; index < 26; ++index)
        str3 += Convert.TpString((object) this.textBox2.Text[index]);
      // uint uint32_3 = Convert.ToUInt32(str3, 16);
      // uint num1 = ytrewq.qwerty(Form1.dfgsf(this.textBox1.Text));
      // uint hashCode = (uint) this.textBox1.Text.GetHashCode();
      // uint fsfsdf = uint32_3 ^ hashCode;
      // this.yreee[0] = uint32_1;
      // this.yreee[1] = uint32_2;
      // this.yreee[2] = uint32_1;
      // this.yreee[3] = uint32_2;
      for (uint i = 0; i < 0xffffffff; i++){
        uint uint32_3 = i;
        uint num1 = ytrewq.qwerty(Form1.dfgsf(this.textBox1.Text));
       uint hashCode = (uint) this.textBox1.Text.GetHashCode();
       uint fsfsdf = uint32_3 ^ hashCode;
       this.yreee[0] = uint32_1;
       this.yreee[1] = uint32_2;
       this.yreee[2] = uint32_1;
       this.yreee[3] = uint32_2;
       if (!this.vxzzz(this.yreee, this.ewrrr, 2415796773U, fsfsdf) || (int) this.yreee[2] != (int) hashCode || (int) this.yreee[3] != (int) num1)
        return;
      int num2 = (int) MessageBox.Show("Congratulations, mate!", "Fine!", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
      }
```

`시리얼 :  28BF522F-A5BE61D1-11E051D1`
