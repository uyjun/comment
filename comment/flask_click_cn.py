from flask import Flask,render_template,request
from clickhouse_cn import Click
app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello world'
# @app.route('/submit_query')
# def submit_query():
#     return render_template("query.html")

@app.route("/querycn",methods=['POST','GET'])
def query():
    # return 'hello'
    if request.method =="POST":
        # results = request.form
        print('choosetext',request.form.get('choosetext'))
        print('querytext', request.form.get('querytext'))
        click = Click()
        # results1 = click.getdata('commentId','b10322c1a5b645a892dd7a8291ee5733')
        results1 = click.getdata(request.form.get('choosetext'),request.form.get('querytext'))

        print("results1:",results1)
        # return 'success'
        return render_template("querycn.html",results=results1)
    return render_template("querycn.html")
# app.route("/delete")
# def delete():
#     commentId = request.args.get("commnetId")
#     click = Click
#     click.deletedata(commentId)
#     return render_template("query.html")
if __name__ == '__main__':
    app.run(debug= True,port=5555,host='127.0.0.1')