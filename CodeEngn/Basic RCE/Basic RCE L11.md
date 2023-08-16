> OEP를 찾으시오. Ex) 00401000 / Stolenbyte 를 찾으시오.
> Ex) FF35CA204000E84D000000 정답인증은 OEP+ Stolenbyte
> Ex ) 00401000FF35CA204000E84D000000

![1](https://github.com/king-raccoon/Yoom/assets/78426205/8008d7ca-f18d-4ec3-8726-30546048104e)
![2](https://github.com/king-raccoon/Yoom/assets/78426205/5b22c524-7d2e-48cb-8d38-08c44ed9b9c1)
![3](https://github.com/king-raccoon/Yoom/assets/78426205/642535d3-e951-4892-9ce5-a5bd12e787ce)
![4](https://github.com/king-raccoon/Yoom/assets/78426205/d8c89102-180c-4bc7-afb6-ddf18c37a0cd)
![5](https://github.com/king-raccoon/Yoom/assets/78426205/113332fe-5e21-4949-b7fb-ba40bc5eebe1)
popad와 jmp 사이 push가 stolenbyte이다.

stolenbyte OPCODE : 6A0068002040006012204000

![6](https://github.com/king-raccoon/Yoom/assets/78426205/2b007fd4-83ef-4eab-8e2c-621423e7b169)
UPX 언패킹 후 다시 디버깅하면 다음과 같이 뜨면서 OEP를 찾을 수 있다

OEP : 00401000

`답 : 004010006A0068002040006812204000`
