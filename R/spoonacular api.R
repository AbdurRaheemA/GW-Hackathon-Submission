library(tidyverse)
library(httr2)
library(jsonlite)
library(dplyr)


api_key <- "b636cc04cc194061a30d76c28c96d935"

# get a broad list of recipes
resp <- request("https://api.spoonacular.com/recipes/complexSearch") |>
  req_url_query(
    number = 100,
    offset = 0,
    addRecipeInformation = FALSE,
    apiKey = api_key
  ) |>
  req_perform()

data <- resp_body_json(resp, simplifyVector = TRUE)

recipe_list <- as_tibble(data$results)
view(recipe_list)

## get details
ids <- paste(recipe_list$id[1:100], collapse = ",")

resp2 <- request("https://api.spoonacular.com/recipes/informationBulk") |>
  req_url_query(
    ids = ids,
    includeNutrition = TRUE,
    apiKey = api_key
  ) |>
  req_perform()

details <- resp_body_json(resp2, simplifyVector = TRUE)
view(details)
