import urllib.request


class Downloader(object):

    def downloade(self, new_url):
        values = {'CNZZDATA1261728817': '1105819609-1526290483-https%253A%252F%252Fm.imooc.com%252F%7C1526290483',
                  'Hm_lpvt_c92536284537e1806a07ef3e6873f2b3': '1526292738',
                  'Hm_lpvt_f0cfcccd7b1393990c78efdeebff3968': '1526292594',
                  'Hm_lvt_c92536284537e1806a07ef3e6873f2b3': '1526291593',
                  'Hm_lvt_f0cfcccd7b1393990c78efdeebff3968': '1526271608,1526286075',
                  'IMCDNS': '0',
                  'PHPSESSID': '870mgsimc1bn2l5562nckioks4',
                  'UM_distinctid': '1635e17936a80-0a7d795d6a3bd7-444a002e-240000-1635e17936b18',
                  'apsid': 'dmZDdjNzc3MWEwYmExODFmNjUzMWI2MDViYjRmNjkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANjI3NjM3OQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADNhNzEzYmY0NjcyNjBiYzdhMjUwYmVlZmU5NmM2OTc3',
                  'connect.sid': 's%3AXvgE_JEbUyg-o0MA80h9MQkg_HTk5QEg.4plN12zpF9y4AWONByV0vN49Sxs6tKlFT4IsNRsG7ug',
                  'cvde': '5af946eeb6e99-57',
                  'imooc_isnew': '1',
                  'imooc_isnew_ct': '1526271592',
                  'imooc_uuid': 'b687d1f6-1a0d-445f-9629-17ed5d52e0b8',
                  'loginstate': '1'}
        postdata = urllib.parse.urlencode(values).encode()
        user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)' \
                     ' Chrome/66.0.3359.139 Safari/537.36'
        headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
        login_url = 'https://m.imooc.com/account/login'
        if new_url is None:
            return
        #res = urllib.request.urlopen(new_url, postdata, headers)
        res = urllib.request.urlopen(new_url)

        if res.getcode() != 200:
            return None
        return res.read()