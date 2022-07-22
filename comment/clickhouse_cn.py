from clickhouse_driver import Client
class Click(object):
    def __init__(self):
        # self.querytext = querytext
        # self.choosetext = choosetext
        self.client = Client(host='127.0.0.1', port='9000', user='default', password='pwnzen', database='iTunes')
    # def getdata(self,results):
    def getdata(self,choosetext,querytext):
        # choosetext = results['choosetext']
        # querytext = results['querytext']
        # print(choosetext)
        # print(querytext)
        sql1 =  'SELECT * FROM iTunes.comment_cn WHERE '+choosetext
        sql2 = "="+"'"+ querytext +"'"
        sql = sql1+sql2
        print("sql:",sql)
        print(self.client.execute(sql))
        return self.client.execute(sql)