from argparse import Namespace
from flask import Blueprint, request, send_from_directory, jsonify, make_response
from flask import render_template, redirect, url_for, send_file, session, g
from datetime import datetime
from functools import wraps
import csv, os

ex = Blueprint('example', __name__, url_prefix='/')
bk = Blueprint('booksite', __name__, url_prefix='/')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(APP_ROOT, 'static', 'img')
BOOK_LIST = os.path.join(APP_ROOT, 'static', 'txt', 'booklist.csv')
BOOK_RESET = os.path.join(APP_ROOT, 'static', 'txt', 'booklist_reset.csv')

#책 소개 페이지
@ex.route("/")
def root():
    return send_from_directory(directory='templates', path='book_static.html')

# 현재 시간 반환 페이지
@ex.route("/today")
def today():
    return str(datetime.today().strftime('현재 시각은 %Y년 %m월 %d일 %I:%M%p 입니다.'))

# 메소드 테스트 페이지
@ex.route("/method")
def testmethod():
    return send_from_directory(directory='templates', path='test_method.html')

@ex.route("/reqinfo", methods=['GET','POST'])
def getreqinfo():
    if request.method == 'GET': third ='3. query_string'
    elif request.method == 'POST': third ='3. body_data'
    reqinfo = {}
    reqinfo['1. url'] = request.url
    reqinfo['2. method'] = request.method
    reqinfo[third] = {
        'fir':request.values.get('fir', 'no data'),
        'sec':request.values.get('sec', 'no data')
        },
    reqinfo['4. cookie'] = request.headers.get('Cookie','no data')
    reqinfo['5. header'] = {
        'Content-Type':request.headers.get('Content-Type','no data'),
        'User-Agent':request.headers.get('User-Agent','no data'),
        'myheader':request.headers.get('myheader','no data')
        },
    return make_response(jsonify(reqinfo))    

##################
# 책 소개 사이트 #
##################
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('booksite.login'))
        return f(*args, **kwargs)
    return decorated_function

@bk.before_request
def check_login_user():
    user_id = session.get('id')
    if user_id is None:
        g.user = None
    else:
        g.user = user_id

@bk.route("/book")
def book():
    book_list = []
    # CSV 파일에서 책 정보 가져오기
    with open(BOOK_LIST, encoding='utf-8') as f:
        reader = csv.reader(f)       
        for row in reader:
            book_list.append(row)
    return render_template('book_dynamic.html',blist=book_list)

@bk.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userid = request.form['id']
        userpw = request.form['pw']
        if userid == 'ID' and userpw == 'PW':
            session['id'] = userid
            return redirect(url_for('booksite.book'))
        else:
            return redirect(url_for('booksite.login'))
    else:
        return render_template('login.html')

@bk.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('booksite.book'))

# 새 책을 추가했을 때
@bk.route("/addbook",methods=['POST'])
@login_required
def addbook():
    # 파일 저장하기
    file = request.files['file']
    if file.filename == "":
        new_img = 'default.png'
    else:
        new_img = file.filename
        file.save(os.path.join(IMG_DIR,new_img))
    # id 얻기
    with open(BOOK_LIST, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        idnum = len(list(reader))+1
    new_id = 'b'+str(idnum)
    # 책 정보 만들기
    book_info=[
        new_id,
        request.form['ntitle'],
        '출간 '+request.form['ndate'],
        '정가 '+request.form['nprice']+'원',
        new_img
    ]
    # 책 정보를 CSV파일에 쓰고 메인 화면으로 돌아가기
    with open(BOOK_LIST, 'a', encoding='utf-8', newline='') as fp:
        csv.writer(fp).writerow(book_info)
    return redirect(url_for("booksite.book"))

@bk.route("/downcsv")
def downcsv():
    return send_file(BOOK_LIST,
                     mimetype='text/csv',
                     attachment_filename='download_booklist.csv',
                     as_attachment=True, cache_timeout=-1)
    
@bk.route("/reset")
@login_required
def reset():
    # booklist 초기화
    with open(BOOK_RESET, "r", encoding='utf-8') as rfp:
        with open(BOOK_LIST, "w", encoding='utf-8') as wfp:
            csv_str = rfp.read()
            wfp.write(csv_str)
    # 책 이미지 초기화
    with open(os.path.join(IMG_DIR,'reset.txt'), encoding='utf-8') as f:
        reset_list = f.read()
    for file in os.listdir(IMG_DIR):
        if file not in reset_list:
            os.remove(os.path.join(IMG_DIR,file))
    return redirect(url_for("booksite.book"))