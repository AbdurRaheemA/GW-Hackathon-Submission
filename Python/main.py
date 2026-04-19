import Calorie_Estimation, Nutrient_Targets

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
     calories = None
     if request.method == 'POST':
          try:   
               weight = float(input("What is your Weight?"))
               height = float(input("What is your Height?"))
               age = int(input("Enter your age:"))
               gender = str(input("What is your Gender? M or F?"))

               calories = Calorie_Estimation(weight, height, age, gender)

          except ValueError:
               calories = "Invalid Input"

     return render_template('index.html', result=calories)

if __name__ == '__main__':
     app.run(debug=True)
        