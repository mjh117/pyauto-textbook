from flask import Flask

# Flask 객체 생성 --- (1)
app = Flask(__name__)

#'/'에 접근했을 때 --- (2)
@app.route("/")
def root():
    return "Hello!"

#'/test'에 접근했을 때 --- (3)
@app.route("/test")
def test():
    return "Test..."

# 웹 서버 실행  --- (4)   
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
