library(tidyverse)


df <- read_csv("Hackathon_Spreadsheet.csv")






# Reading in data
# recipe <- read_csv("recipe.csv")
# nutrition1 <- read_csv("recipe_details_part_01(in).csv")
# nutrition2 <- read_csv("recipe_details_part_02(in).csv")
# nutrition3 <- read_csv("recipe_details_part_03(in).csv")
# nutrition4 <- read_csv("recipe_details_part_04(in).csv")
# nutrition5 <- read_csv("recipe_details_part_05(in).csv")
# 
# # Combining CSVs into one dataset
# list_nutrition <- list(nutrition1, nutrition2, nutrition3, nutrition4, nutrition5)
# list_clean <- list()
# 
# for(i in list_nutrition){
#   ntable <- i |>
#     filter(!is.na(id)) |>
#     filter(nchar(id) == 6)
#   list_clean <- append(list_clean, list(ntable))
# }
# 
# nutrition <- list_rbind(list_clean)

# Cleaning
