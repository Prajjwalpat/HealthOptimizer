from flask import Flask, render_template, request

app2 = Flask(__name__)

@app2.route('/')
def index():
    return render_template('bmi.html')

@app2.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    weight = float(request.form['weight'])
    height = float(request.form['height'])
    bmi = weight / ((height/100) * (height/100))

    if bmi < 18.5:
        category = 'Underweight'
    elif bmi >= 18.5 and bmi <= 24.9:
        category = 'Normal weight'
    elif bmi >= 25 and bmi <= 29.9:
        category = 'Overweight'
    elif bmi >= 30 and bmi <= 34.9:
        category = 'Obesity Class I'
    elif bmi >= 35 and bmi <= 39.9:
        category = 'Obesity Class II'
    else:
        category = 'Obesity Class III'

    return render_template('bmi.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app2.run(port=5002,debug=True)
