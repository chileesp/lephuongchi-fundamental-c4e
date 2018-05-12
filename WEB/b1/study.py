from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
@app.route('/aboutme')
def index():
    info = {
        'name': 'chi',
        'work': 'fanal',
        'school': 'ftu',
        'hobbies': 'movies, pets, music'
    }
    return render_template ('index1.html', info = info)

@app.route('/school')
def hello():
    return redirect("http://techkids.vn ", code=302)

if __name__ == '__main__':
  app.run(debug=True)
