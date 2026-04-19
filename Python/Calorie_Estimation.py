# Goal of averaging the following equations to calculate
# accurate daily calorie intake

# -- Equations -- #
# Miffline-St Jeor Equation
# Harris-Benedict Equaiton
# Katch_McArdle Equation


def Calorie_Estimation(weight, height, age, gender):

    gender = gender.lower()
    if gender == 'M' or 'm':
            Calorie_Count_Miffline_M = 10 * weight + 6.25 * height - 5 * age + 5
            return Calorie_Count_Miffline_M
    if gender == 'F' or 'f':
            Calorie_Count_Miffline_W = 10 * weight + 6.25 * height - 5 * age - 161
            return Calorie_Count_Miffline_W
    
    if gender == 'M' or 'm':
         Calorie_Count_Harris_M = 88.362 + (13.397*(weight)) + (4.799(height)) - (5.677*(age))
         return Calorie_Count_Harris_M
    if gender == 'F' or 'f':
         Calorie_Count_Harris_W = 447.593 + (9.247 * (weight)) + (3.098(height)) - (4.330*(age))
         return Calorie_Count_Harris_W
    
    if gender == 'M' or 'm':
         Calorie_Count_McArdle_M = 0.407 * weight + 0.267 * height - 19.2
         return Calorie_Count_McArdle_M
    if gender == 'F' or 'f':
         Calorie_Count_McArdle_F = 0.252 * weight + 0.473 * height - 48.3
         return Calorie_Count_McArdle_F
    


    

        

    


