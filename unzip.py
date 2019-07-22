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
            print(file)
            if file == 'History':
                self.pathdic = {'chromehs' : '.\\unziptest\\artifacts\\History'}
            if file == 'Bookmarks':
                self.pathdic = {'chromebm' : '.\\unziptest\\artifacts\\Bookmarks'}
            elif file == 'WebCacheV01.dat':
                self.pathdic = {'ie' : '.\\unziptest\\artifacts\\WebCacheV01.dat'}
            elif file == 'places.sqlite':
                self.pathdic = {'firefox' : '.\\unziptest\\artifacts\\places.sqlite'}
            elif file == 'stickymemo':
                pass

            filename.extract(file, '.\\unziptest\\artifacts')

        filename.close()

def main():

    ziptest = Unzip('C:\\GitProject\\capstone_private\\unziptest\\unziptest.zip')
    ziptest.fopen()

if __name__ == '__main__':
    main()

