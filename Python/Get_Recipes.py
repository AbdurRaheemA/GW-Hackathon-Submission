import pandas as pd
from Calorie_Estimation import Calorie_Estimation
import Nutrient_Targets

# Reads the csv of potential recipies
df = pd.read_csv("R\\Hackathon_Spreadsheet.csv")


# Intended to get from a file provided by the web page
User_Information = {"Height": None,
                    "Weight": None,
                    "Age": None,
                    "Gender": None}

# Mock User Data
temp = []
with open("Python\mock_user_data.txt") as f:
    for i in f:
        temp.append(i)

step = 0
for j in User_Information.keys():
    User_Information[j] = temp[step]
    step+=1

User_Information["Height"] = float(User_Information["Height"])
User_Information["Weight"] = float(User_Information["Weight"])
User_Information["Age"] = float(User_Information["Age"])

# Creates the total daily calories a User should consume
User_Total_Calories = Calorie_Estimation(User_Information["Weight"], 
                                         User_Information["Height"], 
                                         User_Information["Age"], 
                                         User_Information["Gender"])

# Calculations for Food Group Breakdown
User_Nutrients = Nutrient_Targets.Nutrient_Breakdown(User_Information["Age"], User_Total_Calories)
User_Food_Groups = Nutrient_Targets.Nutrient_to_Food_Group(User_Nutrients)

# Compiles information from Calorie_Estimation and Nutrient_Targets
User_Recipe_Criteria = User_Food_Groups
User_Recipe_Criteria["Calories"] = User_Total_Calories

# Dataframe queried for relevent recipes
Recipes = df.query(
    "Calories <= @User_Recipe_Criteria['Calories'] and " # Filters Calories
    "@User_Recipe_Criteria['Fat'][0] <= `Fat (g)` <= @User_Recipe_Criteria['Fat'][1] and " # Filters Fat Range
    "@User_Recipe_Criteria['Carbohydrates'][0] <= `Carbs (g)` <= @User_Recipe_Criteria['Carbohydrates'][1] and " # Filters Carbs Range
    "@User_Recipe_Criteria['Protein'][0] <= `Protein (g)` <= @User_Recipe_Criteria['Protein'][1]" # Filters Protein Range
)

# Plan: Send these rows/links to the web page
print(Recipes)