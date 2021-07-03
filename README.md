# 개요
학교 중앙현관에 설치할 프로그램입니다.

**[star0202/school](https://github.com/star0202/school) 에서 이동됨**

# 목차
- [기능](https://github.com/yjdevs/infomaker#기능)
- [필요한 모듈](https://github.com/yjdevs/infomaker#필요한-모듈)
- [가이드](https://github.com/yjdevs/infomaker#가이드)
- [사용 예시](https://github.com/yjdevs/infomaker#사용-예시)
- [주의사항](https://github.com/yjdevs/infomaker#주의사항)
# 기능
날씨 불러오기(네이버), 음원차트 불러오기(멜론), 급식 불러오기(네이버), 날짜가 바뀌면 업데이트 시키기.

# 필요한 모듈
- [requests](https://github.com/psf/requests)
- [bs4](https://github.com/waylan/beautifulsoup)
- [PyQt5](https://github.com/PyQt5)

# 가이드
[infomaker.py](https://github.com/yjdevs/infomaker/blob/main/infomaker.py)
- 모듈 파일입니다.

[main.py](https://github.com/yjdevs/infomaker/blob/main/main.py)
- 실행 파일입니다(콘솔).

[UI.py](https://github.com/yjdevs/infomaker/blob/main/UI.py)
- 실행 파일입니다(GUI).

[Logo.png](https://github.com/yjdevs/infomaker/blob/main/Logo.png)
- 학교 로고 파일입니다.
```python
weather(str)
```
str의 날씨를 리턴합니다.
```python
music_rank(int)
```
멜론에서 int등 까지의 랭킹을 리턴합니다.
```python
school_menu(str)
```
str에 학교 이름을 입력하면 해당 학교의 급식을 불러옵니다.

# 사용 예시

```python
import infomaker  # 모듈 불러오기

root = infomaker.maker()  # root를 infomaker의 maker 객체로 할당한다

print(root.weather("지역"))  # 날씨 불러오기
print(root.music_rank(10))  # 음원차트 10위까지 불러오기
print(root.school_menu("학교"))  # 급식 불러오기
```

# 주의사항
return된 값이 여려줄일 경우 line1\nline2\n처럼 \n이 포함돼 출력됩니다.

날씨의 경우 지역에 따라서 오류가 날 수 있습니다.

오류 발생시 try문에 따라 그 부분만 스킵하게 됩니다.