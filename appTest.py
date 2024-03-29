#윈도우, 시스템에서 돌아간다
import sys

#PyQt5 모듈 설치.
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MyWindow(QWidget):  #QWidget 클래스를 상속 받는 자식클래스인 MyWindow 클래스 선언
    def __init__(self): #생성자(초기화자) 선언
        super().__init__()  #부모 클래스의 생성자 호출
        self.initUI()   #initUI 함수를 자동으로 호출
    
    def initUI(self):
        self.setWindowTitle("나의 파이썬 프로그램")  #윈도우 타이틀 입력
        self.setWindowIcon(QIcon("python.png")) #윈도우 창 아이콘 이미지 불러오기
        # 그래픽모듈 설치.
        self.move(300,300)  #윈도우 창이 시작되는 위치 x, y(픽셀)
        self.resize(300,500) #윈도우 창의 크기 가로 세로

        # 버튼 1제작.
        self.button1 = QPushButton("BUTTON1",self) #버튼 추가. 버튼 이름, self 윈도우판 위에 얹음.
        self.button1.move(100,100) #버튼1번 위치 변경
        self.button1.resize(100,50) #버튼1번 사이즈 변경. 모양, 컬러등 GUI프로그램에서.

        # 텍스트 내용, 위치.
        self.label1 = QLabel("HELLO WORLD", self)
        self.label1.move(105,220)

        self.button1.clicked.connect(self.btn1_click)
        #button1이 클릭되는 이벤트가 발생하면 btn1_click 메서드가 호출됨

        # 버튼 2제작.
        self.button2 = QPushButton("BUTTON2",self)
        self.button2.move(100,300)
        self.button2.resize(100,50)

        self.button2.clicked.connect(self.btn2_click)
        # button2이 클릭되는 이벤트가 발생하면 btn1_click 메서드가 호출됨

        self.show()  # 윈도우 창을 화면에 보여줌

    # 클릭 이벤트
    def btn1_click(self):
        # print("hello world") #버튼과 호출할 메서드를 연결시켜주는 명령어 connect
        self.label1.setText("LOVE PYTHON")

    def btn2_click(self):
        # print("hello world")
        self.label1.setText("HELLO WORLD")


if __name__ == "__main__": #다른곳에서 import할 때 필요한 구문
    app = QApplication(sys.argv)
    win = MyWindow()
    sys.exit(app.exec_())   #창을 닫아주는 명령어.

################# 판 실행 #######################
# 어플들 디자인 작업은 파워포인트 같은 툴이 있어서 연결해서 사용
# Qt Designer (https://build-system.fman.io/qt-designer-download)