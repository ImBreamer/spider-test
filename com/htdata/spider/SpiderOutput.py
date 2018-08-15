from com.htdata.persistence import SqlManager


class DataOuput(object):
    def __init__(self):
        self.datas = []

    def save(self, page_data):
        if page_data is None:
            return
        self.datas.append(page_data)

    def output_data(self):
        sql_manager = SqlManager.DbSqlManager()
        for data in self.datas:
            sql_manager.insert(data)

        sql_manager.down()

    def output_video_data(self):
        for data in self.datas:
            print("craw: " + data)