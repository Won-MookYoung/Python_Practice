from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys

#디자인파일경로
UI_PATH = '06. gui개발/design.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH, self)

        # 버튼 클릭 이벤트
        # self.객체이름.clicked.connect(self.실행할함수이름)
        self.login_btn.clicked.connect(self.login_start)
    def login_start(self):
        #print('로그인버튼 클릭됨')
        input_id=self.id.text()
        input_pw=self.pw.text()
        print('아이디', input_id)
        print('비밀번호', input_pw)

QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())