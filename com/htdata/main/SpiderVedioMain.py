from com.htdata.spider import SpiderDownloader, SpiderParser, SpiderUrlManager, SpiderOutput


class SpiderMain(object):

    def __init__(self):
        self.urls = SpiderUrlManager.UrlManager()
        self.parser = SpiderParser.Parser()
        self.downloader = SpiderDownloader.Downloader()
        self.dataOutput = SpiderOutput.DataOuput()

    def craw(self, start_url):
        self.urls.add_new_url(start_url)
        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print("craw: " + new_url)
                page_content = self.downloader.downloade(new_url)
                new_urls, page_data = self.parser.parser_video(new_url, page_content)
                self.urls.add_new_urls(new_urls)
                self.dataOutput.save(page_data)
                if count == 30000:
                    break

                count = count + 1
            except:
               print("craw failed")

        self.dataOutput.output_video_data()

if __name__ == "__main__":
    startUrl = "https://www.imooc.com/learn/790"
    spiderClient = SpiderMain()
    spiderClient.craw(startUrl)