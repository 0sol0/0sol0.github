from flask import Flask, render_template, jsonify, g, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbKGZ

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def show_member():
    members = list(db.members.find({}, {'_id': False}))
    return jsonify({'all_members': members})

@app.route('/show_update', methods=['GET'])
def show_member_update():
    members = list(db.members.find({}, {'_id': False}))
    return jsonify({'all_members': members})

@app.route('/update', methods=['POST']) #Type을 설정하고,
def update_data():  #POST 요청 확인 Ajax에 data를 요청한다
    update_name_receive = request.form['update_name_give']
    update_date_receive = request.form['update_date_give']
    update_hobby_receive = request.form['update_hobby_give']
    update_mbti_receive = request.form['update_mbti_give']
    update_advantage_receive = request.form['update_advantage_give']
    update_jobstyle_receive = request.form['update_jobstyle_give']
    update_comment_receive = request.form['update_comment_give']
    update_blogurl_receive = request.form['update_blogurl_give']
    update_password_receive = request.form['update_password_give']

    insert_name = db.members['name']
    insert_date = db.members['date']
    insert_hobby = db.members['hobby']
    insert_mbti = db.members['mbti']
    insert_advantage = db.members['advantage']
    insert_jobstyle = db.members['jobstyle']
    insert_comment = db.members['comment']
    insert_blogurl = db.members['blogurl']
    insert_password = db.members['password']

  
    db.members.update_many( #doc에 값을 넣어준다
                            {'name':insert_name}, {"$set":{'name':update_name_receive}},
                            {'date':insert_date}, {"$set":{'date':update_date_receive}},
                            {'hobby':insert_hobby}, {"$set":{'hobby':update_hobby_receive}},
                            {'mbti':insert_mbti}, {"$set":{'mbti':update_mbti_receive}},
                            {'advantage':insert_advantage}, {"$set":{'advantage':update_advantage_receive}},
                            {'jobstyle':insert_jobstyle}, {"$set":{'jobstyle':update_jobstyle_receive}},
                            {'comment':insert_comment}, {"$set":{'comment':update_comment_receive}},
                            {'blogurl':insert_blogurl}, {"$set":{'blogurl':update_blogurl_receive}},
                            {'password':insert_password}, {"$set":{'password':update_password_receive}}
        )
    return jsonify({'result':'success', 'msg': '저장 완료!'})

@app.route('/insert', methods=['POST']) #Type을 설정하고,
def insert_data():  #POST 요청 확인 Ajax에 data를 요청한다
    insert_name_receive = request.form['insert_name_give']
    insert_date_receive = request.form['insert_date_give']
    insert_hobby_receive = request.form['insert_hobby_give']
    insert_mbti_receive = request.form['insert_mbti_give']
    insert_advantage_receive = request.form['insert_advantage_give']
    insert_jobstyle_receive = request.form['insert_jobstyle_give']
    insert_comment_receive = request.form['insert_comment_give']
    insert_blogurl_receive = request.form['insert_blogurl_give']
    insert_password_receive = request.form['insert_password_give']
    
    doc_insert = { #doc에 값을 넣어준다
                    'name':insert_name_receive,
                    'date':insert_date_receive,
                    'hobby':insert_hobby_receive,
                    'mbti':insert_mbti_receive,
                    'advantage':insert_advantage_receive,
                    'jobstlye':insert_jobstyle_receive,
                    'comment':insert_comment_receive,
                    'blogurl':insert_blogurl_receive,
                    'password':insert_password_receive
    }

    db.members.insert_one(doc_insert) #db - members에 doc 값을 넣어준다
    return jsonify({'result':'success', 'msg': '저장 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)