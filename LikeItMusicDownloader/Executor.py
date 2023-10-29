#-*- coding: euc-kr -*-

from Downloader import LMDDownloader
from Convertor import LMDConvertor

class LMDExecutor:
    def __init__(self, url_list, save_dir:str = ""):
        self.url_list = url_list;
        self.save_dir = save_dir;

    # 여러개의 음악을 한번에 다운받고 싶으면 이 부분을 스레드로 만들면 될듯.
    def DownLoad(self):
        try:
            for url in self.url_list:
                if "http" not in url:
                    # 이런 에러나 잘못된 부분에서 log를 남겨놔야 하는데, 일단 넘어가도록 continue로 해두자.
                    continue;
                lmddownloader = LMDDownloader(url, self.save_dir)
                title, down_path = lmddownloader.Download();
                lmdconvertor = LMDConvertor(title, down_path);
                lmdconvertor.Convert();
        except BaseException as e:
            print(str(e))
       
