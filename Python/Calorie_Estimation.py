# Goal of averaging the following equations to calculate
# accurate daily calorie intake

# -- Equations -- #
# Miffline-St Jeor Equation
# Harris-Benedict Equaiton
# Katch_McArdle Equation


def Calorie_Estimation(weight, height, age, gender):

     gender = gender.lower()
     if gender == 'M' or 'm':
          mifflin =  10 * weight + 6.25 * height - 5 * age + 5
          harris = 88.362 + (13.397*(weight)) + (4.799*(height)) - (5.677*(age))
          mcardle = 0.407 * weight + 0.267 * height - 19.2

          average = (mifflin + harris + mcardle ) / 3
          
     elif gender == 'F' or 'f':
          mifflin = 10 * weight + 6.25 * height - 5 * age - 161
          harris = 447.593 + (9.247 * (weight)) + (3.098*(height)) - (4.330*(age))
          mcardle = 0.252 * weight + 0.473 * height - 48.3

          average = (mifflin + harris + mcardle ) / 3
            
     else:
          return "Invalid"
    
     return round(average, 2)


    

        

    


