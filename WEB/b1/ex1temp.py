from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/bmiren/<int:weight>/<int:height>')

def bmiren(weight, height):
    heightm = height / 100
    BMI = weight / (heightm * heightm)

    return render_template('index2.html', BMI=BMI)

if __name__ == '__main__':
  app.run(debug=True)
