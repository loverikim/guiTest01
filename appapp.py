
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MyWindow(QWidget):    # QWidget 클래스를 상속 받는 자식클래스인 MyWindow 클래스를 선언
    def __init__(self):     # 생성자(초기화자) 선언
        super().__init__()  # 부모클래스의 생성자 호출
        self.initUI()       # initUI 함수를 자동으로 호출

    def initUI(self):
        self.setWindowTitle("나의 파이썬 프로그램")  # 윈도우 타이틀 입력
        self.setWindowicon(QIcon("img.png"))    # 윈도우 창 아이콘 이미지 불러오기
        self.move(300,300)  # 윈도우 창이 시작되는 위치 x, y(픽셀)
        self.resize(500,500)  # 윈도우 창의 크기 가로 세로
        self.show() # 윈도우 창을 화면에 보여줌

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWindow
    sys.exit(app.exec_())