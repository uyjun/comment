from clickhouse_driver import Client


# app = Flask (__name__)
# client =Client(host = '127.0.0.1',port = '9000',user = 'default',password = 'pwnzen',database = 'iTunes')
#
# sql0= "SELECT * FROM iTunes.comment_hw WHERE commentId = 'b10322c1a5b645a892dd7a8291ee5733'"
# try:
#     print(client.execute(sql0))

# @app.route('/query',method=['get'])
# def query():
#     client =Client(host = '127.0.0.1',port = '9000',user = 'default',password = 'pwnzen',database = 'iTunes')
#     print(111)
#     querytext = 'b10322c1a5b645a892dd7a8291ee5733'
#     choosetext = 'commentId'
#     sql1 = 'SELECT * FROM iTunes.comment_hw WHERE (*)='
#     sql2 = "'"+querytext+"'"
#     print("sql:",sql1,choosetext)
# except:
#     print("error")
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
        sql1 =  'SELECT * FROM iTunes.comment_hw WHERE '+choosetext
        sql2 = "="+"'"+ querytext +"'"
        sql = sql1+sql2
        print("sql:",sql)
        print(self.client.execute(sql))
        return self.client.execute(sql)
    # def deletedata(self,commentId):

# if __name__ == '__main__':
#     # commentcrawler = CommentCrawler()
#
#         thread = Click()
#         thread.getdata('b10322c1a5b645a892dd7a8291ee5733', 'commentId')