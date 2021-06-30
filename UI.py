import sys
from PyQt5.QtGui import QIcon
import infomaker
from PyQt5.QtWidgets import *
import datetime

root = infomaker.maker()

# UI창
class UI(QWidget):
    def __init__(self, weather, musicrank, schoolmenu):
        super().__init__()
        self.weather = weather
        self.music = musicrank
        self.menu = schoolmenu

        # window size & position
        self.top = 100
        self.left = 500
        self.width = 900
        self.height = 600
        self.setGeometry(self.left, self.top, self.width, self.height)

        # window title & icon
        self.setWindowTitle('서울 양전초등학교 정보 프로그램')
        self.setWindowIcon(QIcon('Logo.png'))

        # background color
        self.setStyleSheet("background-color: white;")

        # call lables()
        self.labels()

    # weather, music rank, school menu labels
    def labels(self):

        # weather
        weatherTitle = QLabel('오늘의 날씨', self)
        weatherlabel = QLabel(self.weather, self)

        # music ranking
        musicTitle = QLabel('멜론 차트 랭킹', self)
        musiclabel = QLabel(self.music, self)

        # school menus
        menuTitle = QLabel('학교 급식', self)
        menulabel = QLabel(self.menu, self)

        # title font
        font1 = weatherTitle.font()
        font1.setPointSize(30)
        font1.setBold(True)
        font1.setFamily('맑은 고딕')

        # text font
        font2 = weatherlabel.font()
        font2.setPointSize(12)
        font2.setFamily('맑은 고딕 Semilight')

        # apply title labels to font1
        weatherTitle.setFont(font1)
        musicTitle.setFont(font1)
        menuTitle.setFont(font1)

        # apply text labels to font2
        weatherlabel.setFont(font2)
        musiclabel.setFont(font2)
        menulabel.setFont(font2)

        grid = QGridLayout()

        # register labels to grid
        grid.addWidget(weatherTitle)
        grid.addWidget(weatherlabel)
        grid.addWidget(musicTitle)
        grid.addWidget(musiclabel)
        grid.addWidget(menuTitle)
        grid.addWidget(menulabel)
        self.setLayout(grid)

if __name__ == '__main__':
    if datetime.date.today() != root.start:
        root.start = datetime.date.today()
        weather = root.weather("개포동")
        musicRank = root.music_rank(5)
        schoolMenu = root.school_menu("양전초등학교")
        app = QApplication(sys.argv)
        # UI 객체 불러오기
        win = UI(weather, musicRank, schoolMenu)
        # 창 보여주기
        win.show()
        app.exec_()
