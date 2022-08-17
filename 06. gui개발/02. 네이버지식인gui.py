from PyQt5.QtWidgets import *
from PyQt5 import uic
import sys
import requests
from bs4 import BeautifulSoup
import openpyxl

#디자인파일경로
UI_PATH = '06. gui개발/design2.ui'

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self,None)
        uic.loadUi(UI_PATH, self)

        # 버튼 클릭 이벤트(추출시작버튼클릭)
        # self.객체이름.clicked.connect(self.실행할함수이름)
        self.start_btn.clicked.connect(self.search)
        self.reset_btn.clicked.connect(self.reset)
        self.save_btn.clicked.connect(self.save)
        self.close_btn.clicked.connect(self.close)
    
    #추출시작
    def search(self):
        # 키워드, 페이지
        keyword = self.keyword.text()     #self 뒤에 애들은 gui 애들가져온거
        page = int(self.page.text())

        for p in range(1, page + 1):
            response = requests.get(f"https://kin.naver.com/search/list.naver?query={keyword}&page={p}")
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 질문 10개 (태그객체)
            lis = soup.select(".basic1 > li")
            i = 1
            for li in lis:
                # 링크태그
                anchor = li.select_one("._searchListTitleAnchor") # dt > a 가능

                # 제목
                title = anchor.text

                # 링크
                link = anchor.attrs['href']

                # 날짜
                date = li.select_one(".txt_inline").text

                # 상세 페이지 요청
                response = requests.get(link)
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')

                # 예외처리 
                try:
                    # 오류가 날만한 코드
                    content = soup.select_one(".c-heading__content").text.strip()
                except:
                    # 실제로 오류가 났을 때 실행되는 코드
                    # 본문이 없는 경우
                    content = ""

                self.textBrowser.append(title)
                self.textBrowser.append(link)
                self.textBrowser.append(date)
                self.textBrowser.append(content)
                QApplication.processEvents()

    #리셋
    def reset(self):
        self.keyword.setText('')    #텍스트 빈걸로 만들기
        self.page.setText('')
        self.textBrowser.setText('')

    #저장
    def save(self):
        result = self.textBrowser.toPlainText()
        f = open(f'06. gui개발/{self.keyword.text()}.txt','w',encoding='utf-8')
        f.write(result)
        f.close()

    #종료
    def close(self):
        sys.exit()
        

QApplication.setStyle('fusion')
app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()
sys.exit(app.exec_())