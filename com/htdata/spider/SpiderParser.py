import re

from bs4 import BeautifulSoup


class Parser(object):
    def parser_url(self, new_url, page_content):
        if new_url is None or page_content is None:
            return
        soup = BeautifulSoup(page_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url, soup)
        return new_urls

    def parser(self, new_url, page_content):
        if new_url is None or page_content is None:
            return
        soup = BeautifulSoup(page_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(new_url, soup)
        new_data = self._get_new_data(new_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, new_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/article/\d+/\d+\.html"))
        for link in links:
            new_url = link['href']
            new_full_url = "http://www.gongkong.com" + new_url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, new_url, soup):
        # <h1 id="Rtitle_D">剑杆织机采用变频调速使用情况</h1>
        res_data = {}
        if new_url == "http://www.gongkong.com/use/QueryLink/?http://www.gongkong.com/" \
                      "gongkong2/use/QueryLink&sTypeValue=1":
            return

        # url
        res_data['url'] = new_url
        # artitle_id
        new_str = re.sub("\D", "", new_url)
        res_data['artitle_id'] = new_str
        # title
        title_node = soup.find('div', class_="product_title").find("h1")
        res_data['title'] = title_node.get_text()
        # writer
        writer_node = soup.find('a', class_="f1405")
        if writer_node is None:
            res_data['writer'] = 'null'
        else:
            res_data['writer'] = writer_node.get_text()

        # readcount
        readcount_node = soup.find('span', class_="detail_Hit")
        res_data['readcount'] = readcount_node.get_text().split('：')[1]

        # createtime
        retimr = re.compile('(\d{2}-\d{2}\d{2}:\d{2}:\d{2})|((\d{2}|\d{1}):(\d{2}|\d{1}):(\d{2}|\d{1}))')
        createtime_node = soup.find('span',text=retimr)
        if createtime_node is None:
            res_data['createtime'] = 'null'
        else:
            res_data['createtime'] = createtime_node.get_text()

        # keyword
        keyword_nodes = soup.find_all('a', class_="f_14")
        keystrs = []
        for keyword_nod in keyword_nodes:
            keystrs.append(keyword_nod.get_text())
        res_data['keyword'] = ','.join(keystrs)

        # remake
        remake_node = soup.find('a', class_="f_14").find_parent('li').find_next_sibling('li').find('span')
        if remake_node is None:
            res_data['remake'] = 'null'
        else:
            res_data['remake'] = remake_node.get_text()


        # maincontent
        maincontent_nodes = soup.find('div', class_='text11').find_all('p')
        maincontent_nodesstrs = []
        for maincontent_node in maincontent_nodes:
            maincontent_nodesstrs.append(maincontent_node.get_text())
        res_data['maincontent'] = ''.join(maincontent_nodesstrs)

        return res_data

    def parser_video_url(self, new_url, page_content):
        if new_url is None or page_content is None:
            return
        soup = BeautifulSoup(page_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_video_urls(new_url, soup)
        return new_urls

    def parser_video(self, new_url, page_content):
        if new_url is None or page_content is None:
            return
        soup = BeautifulSoup(page_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_video_urls(new_url, soup)
        new_data = self._get_new_video_data(new_url, soup)
        return new_urls, new_data

    def _get_new_video_urls(self, new_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/video/\d+"))
        for link in links:
            new_url = link['href']
            new_full_url = "https://m.imooc.com" + new_url
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_video_data(self, new_url, soup):
        # <h1 id="Rtitle_D">剑杆织机采用变频调速使用情况</h1>
        res_data = {}
        if new_url == "https://www.imooc.com/learn/790":
            return

        # srcUrl
        title_node = soup.find('div', id="video-box-mocoplayer-hls-video")
        # srcUrl = title_node.get('src')
        res_data['src'] = title_node

        return res_data