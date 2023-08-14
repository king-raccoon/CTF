<https://dreamhack.io/wargame/challenges/120>

<img width="730" alt="스크린샷 2023-07-05 오전 8 37 31" src="https://github.com/king-raccoon/write-up/assets/78426205/4f9b6921-d10b-4e48-8ed3-c46cfc51e71b">
코드에서 Person class를 보면 g를 2로 설정했음을 알 수 있다.

앨리스가 밥에게 전송할 A = 2^a mod p를 중간자가 A’ = 2^x mod p로 보내고, 2^ax mod p를 계산

밥이 앨리스에게 전송할 B = 2^b mod p를 중간자가 B’ = 2^x mod p로 보내고, 2^bx mod p를 계산

터미널에 c host3.dreamhack.games 15710을 입력하면 위의 사진처럼 나오고, 코드 상 앨리스와 밥의 k를 입력받는데 그게 같으면 암호화된 flag를 얻을 수 있어 각각 1을 입력했다
<img width="217" alt="스크린샷 2023-07-05 오후 6 51 40" src="https://github.com/king-raccoon/write-up/assets/78426205/e701e7d9-8c6a-49d9-91a4-633fa5f26439">
