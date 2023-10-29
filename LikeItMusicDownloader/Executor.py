#-*- coding: euc-kr -*-

from Downloader import LMDDownloader
from Convertor import LMDConvertor

class LMDExecutor:
    def __init__(self, url_list, save_dir:str = ""):
        self.url_list = url_list;
        self.save_dir = save_dir;

    # �������� ������ �ѹ��� �ٿ�ް� ������ �� �κ��� ������� ����� �ɵ�.
    def DownLoad(self):
        try:
            for url in self.url_list:
                if "http" not in url:
                    # �̷� ������ �߸��� �κп��� log�� ���ܳ��� �ϴµ�, �ϴ� �Ѿ���� continue�� �ص���.
                    continue;
                lmddownloader = LMDDownloader(url, self.save_dir)
                title, down_path = lmddownloader.Download();
                lmdconvertor = LMDConvertor(title, down_path);
                lmdconvertor.Convert();
        except BaseException as e:
            print(str(e))
       
