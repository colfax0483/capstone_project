from Morpheme import *
import operator
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc  #한글폰트를 지원받기 위해 사용
import pytagcloud #C:\Users\LOGOS-J\AppData\Local\Programs\Python\Python36\Lib\site-packages\pytagcloud\fonts
import webbrowser
import itertools

class Visualization():
    def __init__(self, wordInfo, filename = None):

        self.wordinfo = wordInfo
        self.filename = filename or "wordcloud.png"
        self.newdict = {}
        self.newdict2 = {}

    def showGraph(self): #wordlist 딕셔너리 형식의 데이터를 받아 막대 그래프를 그리는 함수
        font_fname = 'C:\\Windows\\Fonts\\gulim.ttc'
        font_name = font_manager.FontProperties(fname=font_fname).get_name()
        rc('font', family=font_name)

        plt.xlabel('주요 단어')
        plt.ylabel('빈도수')
        plt.grid(True)

        Sorted_Dict_Values = sorted(self.values(), reverse = True) #최대빈도부터 표현하기 위하여 sorted()함수 사용
        Sorted_Dict_Keys = sorted(self, key=self.get, reverse = True)

        plt.bar(range(len(self)), Sorted_Dict_Values) # 함수는 막대 그래프를 그리는 함수, 필수 인자로 X축, 데이터 리스트값(인덱스에 해당하는 데이터값) 막대그래프의 폭(width), 색상(color), 에러편차값(yerr)등
        plt.xticks(range(len(self)), list(Sorted_Dict_Keys), rotation='70') #x축의 각 데이터별 문자열을 지정

        plt.show()

    def wordCloud(self):

        self.newdict = dict(sorted(self.wordinfo.items(), key=operator.itemgetter(1), reverse=True))
        self.newdict2 = dict(itertools.islice(self.newdict.items(), 20))
        # print(self.newdict)
        taglist = pytagcloud.make_tags(self.newdict2.items(), maxsize=100)
        pytagcloud.create_tag_image(taglist, self.filename, size=(600, 480), fontname='Korean', rectangular=False, layout = pytagcloud.LAYOUT_MOST_HORIZONTAL)

        # webbrowser.open(self.filename)

        return True



def main():
    # wordlist = ["공연음란죄는 범죄이다.", "고슴도치는 귀엽다.", "보이스피싱은 범죄이다.", "범죄자는 위험하다.", "보이스피싱의 범죄자는 연변사람이다.", "보이스피싱은 최근 급증하고 있다."]
    wordlist = ["살해", "살해", "살해", "살해", "살해", "살해", "살해", "살해", "방화", "방화", "방화", "방화", "방화", "방화", "방화", "방화", "방화", "사건", "사건", "사건", "사건", "사건", "사건", "사건", "범죄", "범죄", "범죄", "범죄", "범죄",
     "범죄", "범죄", "사회", "사회", "사회", "사회", "사회", "사회", "사회", "밀실살인", "밀실살인", "밀실살인", "밀실살인", "밀실살인", "농약", "농약", "농약", "농약", "몰래카메라", "뉴스",
     "뉴스", "뉴스", "뉴스", "스토커", "스토커", "스토커", "스토커", "의사", "의사", "의사", "아내", "아내", "아내", "아내", "방법", "방법", "방법", "아파트", "아파트", "연탄"]

    test = Morpheme(wordlist)
    wordInfo = test.parser()

    a = Visualization(wordInfo, "wordcloud.png")
    #b = a.showGraph()
    a.wordCloud()

if __name__ == '__main__':
    main()

