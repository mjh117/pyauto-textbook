from flask import Flask
import glob

# Flask 객체 생성--- (*1)
app = Flask(__name__)

#'/'에 접근했을 때 --- (*2)
@app.route("/")
def root():
    # 파일 목록 가져오기 --- (*3)
    files = glob.glob('static/*')
    # HTML에 파일 링크 표시 --- (*4)
    html = '<html><meta charset="utf-8"><body>'
    html += '<h1>파일 목록</h1>'
    for f in files:
        html += '<p><a href="{0}">{0}</a></p>'.format(f)
    html += '</body></html>'
    return html

# 웹 서버 기동 --- (*5)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
