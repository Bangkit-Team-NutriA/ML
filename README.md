# ML

All About code for bangkit academy capstone expecially Machine Learning

We have 3 features using Machine Learning Approach:
- Food Image Classification
  - we merge data from [food 101](https://www.kaggle.com/datasets/      kmader/food41) and [indonesia food](https://www.kaggle.com/datasets/robertusbagaskara/indonesian-food-image
and merge it)
  - we just took 7 labels from indonesian food, so there is 108 labels
  - we do transfer learning using efficientNetV2L and Resnet 50
- Meal Recommendation  
  - we use data that we scrape from [panganku.org](https://www.panganku.org).
  - we use genetic algorithm to search best combination for food to be recommend.
  - we penalize fat and carbohydrate more than protein and calories so the recommendation will be strict to them both than protein and calories.
  - you can find the code in here [code](meal)
- Recipe Recommendation
  - we use data that we scrape from [fatsecret.co.id](https://www.fatsecret.co.id)
  - we transform all ingredients in dataset to list and do bag of word from [this](dataset/dataRecipe.json) into [this](dataset/setForJaccard.json).
  - we use modified jaccard index to find the closest distance, so instead of using union we just take the length of ingredients we calculate with.
  - you can find the code in here [code](recipe)


