import pymysql


class DbSqlManager(object):
    def __init__(self):
        self.db_client = pymysql.connect(host='192.168.1.112', user='root', password='theta123', db='iiotapp_mobile', charset='utf8')
        # self.db_client = pymysql.connect(host='192.168.0.83', user='root', password='1234qwer', db='htiiot', charset='utf8')
        self.cursor = self.db_client.cursor()

    def insert(self, page_data):
        try:
            sql = "INSERT INTO mobile_manager_knowledge(article_id,url,writer,title,keyword,remake,main_content,read_count,create_time) VALUES('%s', '%s','%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            page_data['artitle_id'], page_data['url'], page_data['writer'], page_data['title'], page_data['keyword'],
            page_data['remake'], page_data['maincontent'], page_data['readcount'], page_data['createtime'])
            print(sql)
            self.cursor.execute(sql)
        except:
            print('insert failed')

    def insert_person(self, p_id, edu, person, skill):
        try:
            if edu is None:
                print('insert null')
            else:
                sql = "INSERT INTO  mobile_person_resume(id,NAME,gender,birthday,education,graduate_school,major,major_start,major_end,work_life,marital_status,political_outlook,residence,origin,mobile,email,skill,create_time) VALUES('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                      % (int(p_id), person['membername'], person['sex'], person['birthday'], person['xueli'], person['schoolname'], person['majorName'], edu['StartTime'], edu['EndTime'], person['workyear'], person['maritalstatus'], person['zzmm'], person['juzhudi'], person['hukou'], person['mobilephone'], person['email'], skill, person['CreateTime'],)
                print(sql)
                self.cursor.execute(sql)
        except:
            print('insert failed')

    def insert_person_worklife(self, p_id, work):
        try:
            if work is None:
                print('insert null')
            else:
                sql = "INSERT INTO mobile_person_worklife(person_id,start_time,end_time,company,work_position,work_content) VALUES('%d','%s','%s','%s','%s','%s')" \
                      % (int(p_id),  work['StartTime'], work['EndTime'], work['CompanyName'], work['JobName'], work['WorkContent'])
                print(sql)
                self.cursor.execute(sql)
        except:
            print('insert failed')

    def insert_order_info(self,order_id, order_info, order_auto):
        try:
            sql = "INSERT INTO mobile_order_info(id,NAME,STATUS,material,thickness,COUNT,maxprice,is_material,imgurl,remakes,tel,lng,lat,create_time) VALUES('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" \
                  % (int(order_id), order_info['Name'], order_info['State'], order_info['Material'], order_info['Thickness'], order_info['Count'], order_info['MaxPrice'], order_info['IsMaterial'], order_info['PhotoStr'], order_info['Remarks'], order_info['Tel'], order_auto['Lng'], order_auto['Lat'], order_info['CreateTime'])
            print(sql)
            self.cursor.execute(sql)
        except:
            print('insert order failed')

    def down(self):
        self.cursor.close()
        self.db_client.close()



