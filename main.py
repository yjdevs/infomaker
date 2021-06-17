import infomaker
import datetime

root =  infomaker.infomaker()

if __name__ == "__main__":
    while 1:#메인루프
        if datetime.date.today() != root.start:#날짜가 바뀌면 재시작
            root.start = datetime.date.today()
            try:
                print(root.weather("개포동"))
                print(root.music_rank(5))
                print(root.school_menu("양전초등학교"))
            except Exception as ex:
                print(ex)