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
        self.result = {}
        for line in self.artilist:
            noun_list = self.nlp.nouns(line)

            # 단어 검색 및 추가
            for noun in noun_list:
                if str(noun).isnumeric(): # 숫자만 있으면
                    continue
                elif self.result.get(noun) == None: # 처음 찾아진 단어일 경우
                    self.result[noun] = 1
                # 이미 있는 단어일 경우 --> 카운트 증가
                else:
                    self.result[noun] += 1
        # result = sorted(result.items(), key=lambda x:x[1], reverse=True)

        sum1 = sum(self.result.values())
        total = 0
        for noun in self.result:

            ah = round(self.result[noun] / sum1 * 100, 2)
            print(noun + " : " + str(self.result[noun]) + "회(" + str(ah) + "%)")

        return self.result



def main():
    chrome = ChromeHistory.Chrome('C:\\History')
    history = chrome.visiturl()
    #wordlist = list(history.values())
    # wordlist = ["공연음란죄는 범죄이다.", "고슴도치는 귀엽다.", "보이스피싱은 범죄이다.", "범죄자는 위험하다.", "보이스피싱의 범죄자는 연변사람이다.", "보이스피싱은 최근 급증하고 있다."]
    wordlist = ["설상가상으로 영국에서 아랍의 폭탄테러로 점보 항공기가 폭발하는 사고도 발생했다."]
    # noun_list = nlp.nouns("공연음란죄는 범죄이다.")
    test = Morpheme(wordlist)

    print(test.parser())

if __name__ == '__main__':
    main()