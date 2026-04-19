from Calorie_Estimation import Calorie_Estimation
from Nutrient_Targets import Nutrient_Breakdown, user_age, total_calories


from flask import Flask, render_template, request
import json
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    calories = None
    nutrients = None
    if request.method == 'POST':
        try:   
            weight = float(request.form.get("weight"))
            height = float(request.form.get("height"))
            age = int(request.form.get("age"))
            gender = request.form.get("gender")

            calories = Calorie_Estimation(weight, height, age, gender)
            nutrients = Nutrient_Breakdown(user_age, total_calories)
            
        except ValueError:
            calories = "Invalid Input"
            nutrients = "Invalid"

            

    return render_template('index.html', result=calories, macros=nutrients)

if __name__ == '__main__':
     app.run(debug=True)
        