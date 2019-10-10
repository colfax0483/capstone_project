import warnings
warnings.simplefilter("ignore", UserWarning)
from konlpy.tag import Okt
import ChromeHistory

class Morpheme():
    def __init__(self, artilist):
        if type(artilist) in [list]:
            self.artilist = artilist
        else:
            # raise UnknownTypeException()
            print("Not List")

        self.nlp = Okt()
        self.result = {}

    def parser(self):
        for line in self.artilist:
            noun_list = self.nlp.nouns(line)

            # 단어 검색 및 추가
            for noun in noun_list:
                # 처음 찾아진 단어일 경우
                if self.result.get(noun) == None:
                    self.result[noun] = 1
                # 이미 있는 단어일 경우
                else:
                    self.result[noun] += 1
        # result = sorted(result.items(), key=lambda x:x[1], reverse=True)

        sum1 = sum(self.result.values())
        total = 0
        for noun in self.result:

            ah = round(self.result[noun] / sum1 * 100, 2)
            # print(noun + " : " + str(self.result[noun]) + "회(" + str(ah) + "%)")

        return self.result



def main():
    chrome = ChromeHistory.Chrome('C:\\History')
    history = chrome.visiturl()
    #wordlist = list(history.values())
    wordlist = ["공연음란죄는 범죄이다.", "고슴도치는 귀엽다.", "보이스피싱은 범죄이다.", "범죄자는 위험하다.", "보이스피싱의 범죄자는 연변사람이다.", "보이스피싱은 최근 급증하고 있다."]
    # noun_list = nlp.nouns("공연음란죄는 범죄이다.")
    test = Morpheme(wordlist)

    print(test.parser())

if __name__ == '__main__':
    main()