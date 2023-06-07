from flask import Flask, render_template, request
from datetime import datetime, timedelta

app4 = Flask(__name__)

@app4.route('/')
def index():
    return render_template('preg.html')

@app4.route('/calculate_pregnancy', methods=['POST'])
def calculate_pregnancy():
    last_period = datetime.strptime(request.form['last_period'], '%Y-%m-%d')
    due_date = last_period + timedelta(days=280)

    return render_template('preg.html', result=due_date.strftime('%B %d, %Y'))

if __name__ == '__main__':
    app4.run(port=5004,debug=True)
