import requests
from bs4 import BeautifulSoup
import datetime

class infomaker:
    def __init__(self):
        self.start = None
    def weather(self, location):
        Finallocation = location + ' 날씨'
        CheckDust = []
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + Finallocation
        hdr = {'User-Agent': (
                'mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/78.0.3904.70 safari/537.36')}
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        # 오류 체크
        ErrorCheck = soup.find('span', {'class': 'btn_select'})
        if 'None' in str(ErrorCheck):
            pass#지역 없음
        else:  # 지역 정보
            for i in soup.select('span[class=btn_select]'):
                NowTemp = soup.find('span', {'class': 'todaytemp'}).text + soup.find('span', {'class': 'tempmark'}).text[2:]
                # 날씨 캐스트
                WeatherCast = soup.find('p', {'class': 'cast_txt'}).text
                # 오늘 오전온도, 오후온도, 체감온도
                TodayMorningTemp = soup.find('span', {'class': 'min'}).text
                TodayAfternoonTemp = soup.find('span', {'class': 'max'}).text
                TodayFeelTemp = soup.find('span', {'class': 'sensible'}).text[5:]
                # 미세먼지, 초미세먼지, 오존 지수
                CheckDust1 = soup.find('div', {'class': 'sub_info'})
                CheckDust2 = CheckDust1.find('div', {'class': 'detail_box'})
                for x in CheckDust2.select('dd'):
                    CheckDust.append(x.text)
                FineDust = CheckDust[0][:-2] + " " + CheckDust[0][-2:]
                UltraFineDust = CheckDust[1][:-2] + " " + CheckDust[1][-2:]
                Ozon = CheckDust[2][:-2] + " " + CheckDust[2][-2:]
                result = "날씨 요약:" + WeatherCast + "\n현재온도:" + NowTemp + "\n체감온도:" + TodayFeelTemp + \
                         "\n오전/오후 온도:" + TodayMorningTemp + "/" + TodayAfternoonTemp + "\n현재 상태:" + WeatherCast + \
                         "\n현재 미세먼지 농도:" + FineDust + "\n현재 초미세먼지 농도:" + UltraFineDust + "\n현재 오존 지수:" + Ozon + "\n"
                return result
    def music_rank(self, rank):
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
        req = requests.get('https://www.melon.com/chart/week/index.htm', headers=header)
        html = req.text
        parse = BeautifulSoup(html, 'html.parser')
        titles = parse.find_all("div", {"class": "ellipsis rank01"})#제목
        singers = parse.find_all("div", {"class": "ellipsis rank02"})#가수
        title = []
        singer = []
        for t in titles:
            title.append(t.find('a').text)
        for s in singers:
            singer.append(s.find('span', {"class": "checkEllipsis"}).text)
        result = ""
        for i in range(rank):
            result = result + '%s위:%s - %s' % (i + 1, title[i], singer[i]) + "\n"
        return result
    def school_menu(self, school):
        res = requests.get("https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=" + school + " 급식")
        source = res.text
        soup = BeautifulSoup(source, 'html.parser')
        a = soup.select('.menu_info')#메뉴 불러오기
        dt = datetime.datetime.now()
        today = " " + str(dt.month) + "월 " + str(dt.day) + "일 "
        for menu in a:
            menu_today = menu.text[:menu.text.find('[')]
            if menu_today == today:#오늘거만 불러오기
                menutext = menu.text[1:]
                menutext = menutext.replace("*","")
                result = menutext + "\n"
        try:
            return result
        except Exception:
            return '오늘은 급식이 없습니다'
