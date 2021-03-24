# 설명
DictionaryAttack.py는 자신이 구축한 실습 환경에 사전 공격을 시도할 때 사용하는 스크립트입니다.
사전 파일을 제공하지 않으므로 공격에 필요한 사전 파일이 필요합니다.

# 사용법
$ git clone https://github.com/mer1-97/Dictionary_Attack.git

$ cd Dictionary_Attack

$ pip install -r requirements.txt

$ 스크립트 실행전 해야할 일
* DictionaryAttack.py에 **url** = **'타겟 사이트의 url'** 입력
* userIdDictionary.txt, userPwDictionary.txt에 자신이 가지고 있는 사전 파일 입력

$ python DictionaryAttack.py

$ 공격 성공시 login_ok.txt에 로그인에 성공한 id, pw가 기록됨

# 실행 예시
![image](https://user-images.githubusercontent.com/76419721/112312913-abf30b00-8cea-11eb-9894-1d108de843a4.png)

![image](https://user-images.githubusercontent.com/76419721/112313001-c0370800-8cea-11eb-8bdb-a118071f9934.png)
