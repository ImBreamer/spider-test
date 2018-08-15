import json
import urllib.request

from com.htdata.persistence import SqlManager


class ReadMain(object):
    def __init__(self):
        self.sql_manager = SqlManager.DbSqlManager()

    def get_person(self):
        url = 'http://outwardapi.hence.cn/api/Ta_MemberInfo/getList?Token=d04259b9c0a3ccabedae048c1d3bef3f&Name=&Job=&PageIndex=1&PageSize=10000'
        res = urllib.request.urlopen(url)
        json_str = res.read().decode('utf-8', 'ignore')
        req_json = json.loads(json_str, strict=False)
        data = req_json['data']
        return data

    def get_person_info(self, p_id):
        url = 'http://outwardApi.hence.cn/api/Ta_MemberInfo/getDetail?Token=d04259b9c0a3ccabedae048c1d3bef3f&Id=' + p_id
        res = urllib.request.urlopen(url)
        json_str = res.read().decode('utf-8', 'ignore')
        req_json = json.loads(json_str, strict=False)
        data = req_json['data']
        return data

    def insert_person_run(self):
        people = self.get_person()
        n = 10
        for person in people:
            try:
                personID = person['Id']
                person_kill = ''
                data = self.get_person_info(personID)
                skill_data = data['skill']
                skills = list()
                for skill_one in skill_data:
                    skills.append(skill_one['SkillName'])

                edu_data = data['edu']
                person_kill = ','.join(skills)
                self.sql_manager.insert_person(n, edu_data[0], person, person_kill)
                work_data = data['work']
                for work in work_data:
                    self.sql_manager.insert_person_worklife(n, work)

                n = n + 1
            except:
                print('insert failed')

    def get_order_auto(self):
        url = 'http://outwardApi.hence.cn/api/Requirement/getList?Token=d04259b9c0a3ccabedae048c1d3bef3f&Name=&TimeSort=0&State=0&PageIndex=1&PageSize=10000'
        res = urllib.request.urlopen(url)
        json_str = res.read().decode('utf-8', 'ignore')
        req_json = json.loads(json_str, strict=False)
        data = req_json['data']
        return data

    def get_order_info(self, order_id):
        url = 'http://outwardApi.hence.cn/api/Requirement/getDetail?Token=d04259b9c0a3ccabedae048c1d3bef3f&ID=' + order_id
        res = urllib.request.urlopen(url)
        json_str = res.read().decode('utf-8', 'ignore')
        req_json = json.loads(json_str, strict=False)
        data = req_json['data']
        return data

    def insert_order_run(self):
        orders = self.get_order_auto()
        n = 1
        for order in orders:
            try:
                orderID = order['ID']
                data = self.get_order_info(orderID)
                self.sql_manager.insert_order_info(n, data[0], order)

                n = n + 1
            except:
                print('insert failed')

if __name__ == "__main__":
    readMain = ReadMain()
    readMain.insert_order_run()
