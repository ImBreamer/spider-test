import re

import pymysql
from bs4 import BeautifulSoup

from com.htdata.persistence import SqlManager
from com.htdata.spider import SpiderDownloader, SpiderParser, SpiderUrlManager, SpiderOutput


class SpiderMain(object):

    def __init__(self):
        self.sql_manager = SqlManager.DbSqlManager()
        self.urls = SpiderUrlManager.UrlManager()
        self.parser = SpiderParser.Parser()
        self.downloader = SpiderDownloader.Downloader()
        self.dataOutput = SpiderOutput.DataOuput()

    def craw(self, start_id, start_url):
        page_content = self.downloader.downloade(start_url)
        new_urls = self.parser.parser_url(start_url, page_content)
        for url in new_urls:
            art_id = re.sub("\D", "", url)
            sql = "INSERT INTO operation_relationship_2 (article_id,category_id) VALUES ('%s', '%s')" % (art_id, start_id)
            self.sql_manager.cursor.execute(sql)

if __name__ == "__main__":
    spiderClient = SpiderMain()
    db_client = pymysql.connect(host='192.168.1.112', user='root', password='theta123', db='iiotapp_mobile', charset='utf8')
    cursor = db_client.cursor()
    sql = "SELECT id,url  FROM operation_category_2 WHERE url IS NOT NULL"
    cursor.execute(sql)
    results = cursor.fetchall()
    checks = []
    for row in results:
        cate_id = row[0]
        cate_url = row[1]
        print(cate_url)
        try:
            p_c = spiderClient.downloader.downloade(cate_url)
            soup = BeautifulSoup(p_c, 'html.parser', from_encoding='utf-8')
            root_node = soup.find('div', class_="gkPage")
            if root_node is not None:
                remake_node = root_node.find('span')
                span_text = remake_node.get_text()
                inx = span_text.index('第')
                rand_str = span_text[inx + 1:-1]
                x = rand_str.split('/')
                cate_urls = [cate_url + "&pageSize=10&pageIndex={}".format(str(i)) for i in range(int(x[0]), int(x[1])+1)]
                for c_url in cate_urls:
                    spiderClient.craw(cate_id, c_url)
        except:
            print("craw failed")