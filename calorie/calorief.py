from flask import Flask, render_template, request

app3 = Flask(__name__)

@app3.route('/')
def index():
    return render_template('calorie.html')

@app3.route('/calculate_calories', methods=['POST'])
def calculate_calories():
    gender = request.form['gender']
    age = int(request.form['age'])
    height = int(request.form['height'])
    weight = int(request.form['weight'])
    activity = float(request.form['activity'])
    
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    calories = bmr * activity

    return render_template('calorie.html', result=calories)

if __name__ == '__main__':
    app3.run(port=5003,debug=True)
