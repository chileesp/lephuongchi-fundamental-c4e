from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/bmi/<int:weight>/<int:height>')

def bmi (weight, height):
    heightm = height / 100
    BMI = weight / (heightm * heightm)

    if (BMI < 16):
        condition = "Severely underweight"
    elif (16 <= BMI < 18.5 ):
        condition = "Underweight"
    elif (18.5 <= BMI < 25):
        condition = "Normal"
    elif (25 <= BMI < 30):
        condition = "Overweight"
    else:
        condition = "Obese"

    return "you are: {0}".format(condition)

if __name__ == "__main__":
    app.run(debug=True)
