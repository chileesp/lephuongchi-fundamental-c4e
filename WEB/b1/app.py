#fapp
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') #homepage
def index():
    posts = [
        {
            "title" : "tho con coc",
            "content" : "hihi",
            "author" : "tuan anh",
            "gender" : 1
        },

        {
            "title" : "thơ củ lạc ",
            "content" : "lạy chúa trên cao turndown 4 what",
            "author" : "Nhật minh",
            "gender": 0
        },

        {
            "title" : " em không nghĩ ra ",
            "content" : "  không nghĩ ra gì",
            "author" : "Trường dingtea",
            "gender": 1
        },

        {

            "title" : "  sầm sơn ",
            "content" : "  sầm sơn sóng đánh dập dồn chị em phụ nữ hết mình vui chơi",
            "author" : "Quang Dũng",
            "gender": 1
        }
    ]
    return render_template('index.html', posts=posts) #file index.html

@app.route('/c4e')
def sayhi():
    return "hi c4e 17"

@app.route('/sayhi/<name>/<age>')  #parameter:name == argument in funct
def sayhii(name, age):
    return "hi {0}, you are {1} year olds".format(name, age)

# @app.route('/sum/<a>/<b>')
# def calc(a, b):
#     sum = int(a) + int(b)  #a,b str -> int -> str
#     return str(sum)

# cach2
@app.route('/sum/<int:a>/<int:b>')
def calc(a, b):
    return str(a+b)

if __name__ == '__main__':
  app.run(debug=True) #de...true > auto restart >update
