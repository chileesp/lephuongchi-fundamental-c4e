from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/user/<username>')

def user(username):
    users = {
        "chi": {
            "name" : "chi",
            "age" : 20
        },
        "bibi": {
            "name" : "bibi ",
            "age" : 10
        }
    }
    if username in users.keys():
        return render_template('index3.html', users = users[username])
    else:
        return "not found!!!"

if __name__ == '__main__':
  app.run(debug=True)
