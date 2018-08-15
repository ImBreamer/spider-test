import re

import pymysql

if __name__ == "__main__":
    url = "http://www.gongkong.com/use/DemandLink/?status=1&id=1&brandid=0&industryid=0&productsid=0&parmterid=0&iitype=0&pageIndex=1&pageSize=" + "{}"
    urls = ["http://www.gongkong.com/use/DemandLink/?status=1&id=1&brandid=0&industryid=0&productsid=0&parmterid=0&iitype=0&pageIndex=1&pageSize=" + "{}".format(str(i)) for i in range(1, 11)]
    print(urls)
    # url = "总条数：812 | 当前第1 / 82页"
    # inx = url.index('第')
    # print(inx)
    # inxx = url.index('页')
    # print(inxx)
    # print(url[inx+1:-1])
    # 总条数：812 | 当前第1 / 82页
   # db_client = pymysql.connect(host='192.168.1.112', user='root', password='theta123', db='iiotapp_mobile',charset='utf8')
   # cursor = db_client.cursor()
   # sql = "INSERT INTO knowledge_relationship_2 (article_id,category_id) VALUES ('%s', '%s')" % ('1', '1')
   # print(sql)
   # cursor.execute(sql)
   # results = cursor.fetchall()
   # checks = []
   # for row in results:
   #     item = {}
   #     item['id'] = row[0]
   #     item['url'] = row[1]
   #     checks.append(item)
   #     print(checks)