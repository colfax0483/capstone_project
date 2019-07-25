import zipfile
import os.path

class Unzip:
    def __init__(self, path):
        self.path = path
        self.pathdic = {}

    def fopen(self):
        filename = zipfile.ZipFile(self.path)
        try:
            if zipfile.is_zipfile(self.path) is False:
                raise NotZipFileError
        except NotZipFileError:
            return -1

        for file in filename.namelist(): # 압축파일 내 파일명을 리스트로
            # print(file) 파일명만 출력
            if file == 'History':
                self.pathdic['chromehs'] = '.\\ziptest\\artifacts\\History'
            if file == 'Bookmarks':
                self.pathdic['chromebm'] = '.\\ziptest\\artifacts\\Bookmarks'
            elif file == 'WebCacheV01.dat':
                self.pathdic['ie'] = '.\\ziptest\\artifacts\\WebCacheV01.dat'
            elif file == 'places.sqlite':
                self.pathdic['firefox'] = '.\\ziptest\\artifacts\\places.sqlite'
            elif file == 'stickymemo':
                self.pathdic['stickymemo'] = '.\\ziptest\\artifacts\\plum.sqlite'

            filename.extract(file, '.\\ziptest\\artifacts')

        filename.close()
        return self.pathdic

def main():

    ziptest = Unzip('C:\\GitProject\\capstone_private\\ziptest\\unziptest.zip')
    ziptest.fopen()

if __name__ == '__main__':
    main()

