# Function which takes total calories and breaks it down
# into suggested food groups/nutrient percentages

# Calculated using the following source
# https://www.ncbi.nlm.nih.gov/books/NBK610333/
def Nutrient_Breakdown(user_age, total_calories):
    # --- Calorie Break Up for those above the age of 18 --- #
    if user_age>=18:
        # Fat 20-35
        Upper_Fat = total_calories*0.35
        Lower_Fat = total_calories*0.20
        
        # Linoleic Acid 5-10
        Upper_Linoleic_Acid = total_calories*0.10
        Lower_Linoleic_Acid = total_calories*0.05

        # a Linoleic Acid 0.5-1.2
        Upper_a_Linoleic_Acid = total_calories*0.012
        Lower_a_Linoleic_Acid = total_calories*0.005

        # Carbohydrate 45-65
        Upper_Carbohydrate = total_calories*0.65
        Lower_Carbohydrate = total_calories*0.45

        # Protein 10-35
        Upper_Protein = total_calories*0.35
        Lower_Protein = total_calories*0.10
    
    # --- Calorie Break Up for those between ages 4 to 17 (inclusive) --- #
    elif user_age>=4:
        # Fat 25-35
        Upper_Fat = total_calories*0.35
        Lower_Fat = total_calories*0.25
        
        # Linoleic Acid 5-10
        Upper_Linoleic_Acid = total_calories*0.10
        Lower_Linoleic_Acid = total_calories*0.05

        # a Linoleic Acid 0.6-1.2
        Upper_a_Linoleic_Acid = total_calories*0.012
        Lower_a_Linoleic_Acid = total_calories*0.006

        # Carbohydrate 45-65
        Upper_Carbohydrate = total_calories*0.65
        Lower_Carbohydrate = total_calories*0.45

        # Protein 10-30
        Upper_Protein = total_calories*0.30
        Lower_Protein = total_calories*0.10

    # --- Calorie Break Up for those below the age of 4 --- #
    else:
        # Fat 30-40
        Upper_Fat = total_calories*0.40
        Lower_Fat = total_calories*0.30
        
        # Linoleic Acid 5-10
        Upper_Linoleic_Acid = total_calories*0.10
        Lower_Linoleic_Acid = total_calories*0.05

        # a Linoleic Acid 0.6-1.2
        Upper_a_Linoleic_Acid = total_calories*0.012
        Lower_a_Linoleic_Acid = total_calories*0.006

        # Carbohydrate 45-65
        Upper_Carbohydrate = total_calories*0.65
        Lower_Carbohydrate = total_calories*0.45

        # Protein 5-20
        Upper_Protein = total_calories*0.20
        Lower_Protein = total_calories*0.05

    return {"Fat": (Lower_Fat, Upper_Fat),
            "Linoleic Acid": (Lower_Linoleic_Acid, Upper_Linoleic_Acid),
            "a Linoleic Acid": (Lower_a_Linoleic_Acid, Upper_a_Linoleic_Acid),
            "Carbohydrates": (Lower_Carbohydrate, Upper_Carbohydrate),
            "Protein": (Lower_Protein, Upper_Protein)
            }

# Converts the previously calculated percentages from the 
# Nutrient_Breakdown() function into human-readable information

# Calculated using the following source
# https://www.ncbi.nlm.nih.gov/books/NBK56068/table/summarytables.t4/?report=objectonly
def Nutrient_to_Food_Group(user_age, user_gender, nutrient_breakdown):

    # Converts dictionary to array for easier referencing #
    myArr = []
    for nutrient_group in nutrient_breakdown.keys():
        newRow = []
        for i in nutrient_breakdown[nutrient_group]:
            newRow.append(i)
        myArr.append(newRow)

    # --- Calorie to Food Group (g) for those 6 months or younger --- #
    if user_age<00.5:
        pass
    
    # --- Calorie to Food Group (g) for those 12 months or younger --- #
    elif user_age<=1:
        pass

    # --- Calorie to Food Group (g) for those ages 3 or younger --- #
    elif user_age<=3:
        pass

    # --- Calorie to Food Group (g) for those ages 8 or younger --- #
    elif user_age<=8:
        pass

    elif user_gender == "F":
        pass

    else:
        pass

# Converts body weight to suggested water intake

def Water_Intake(body_weight):
    pass

# Calorie to Grams Calculator
# Maybe make the dictionary a numpy array