> Key를 구한 후 입력하게 되면 성공메시지를 볼 수 있다.  
> 이때 성공메시지 대신 Key 값이 MessageBox에 출력 되도록 하려면 파일을 HexEdit로 오픈 한 다음 0x???? ~ 0x???? 영역에 Key 값을 overwrite 하면 된다.  
> 문제 : Key값과 + 주소영역을 찾으시오  
> Ex) 7777777????????

![1](https://github.com/king-raccoon/Yoom/assets/78426205/46aa2d32-a553-4a6a-b6de-ca60a4ff345e)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/2de48529-c05a-4a8b-9c13-c0843cb93186)
밑으로 내리다보면 성공할 때 나올 것 같은 문자열이 나오는 데 7A2896BFh와 비교를 하고 같으면 그 문구가 출력된다

![3](https://github.com/king-raccoon/Yoom/assets/78426205/b7a7edfb-c71b-4265-8920-6c8927eddc34)
10진수로는 **2049480383** 이다.

10진수로 바꾼 이유는 위에 함수 GetDlgItemInt에서 10진수를 받고 이것과 비교하기 때문이다.

![4](https://github.com/king-raccoon/Yoom/assets/78426205/0966214a-857f-406e-9c9f-09815015e947)

주소영역은 D3B~ D45이다

근데 이때 주소영역이 ????????이므로 0D3B0D45로 한다

`정답 ; **2049480383**0D3B0D45`
