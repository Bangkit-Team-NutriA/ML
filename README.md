# ML

All About code for bangkit academy capstone expecially Machine Learning

We have 3 features using Machine Learning Approach:
- Food Image Classification
  - we merge data from [food 101](https://www.kaggle.com/datasets/kmader/food41) and [indonesia food](https://www.kaggle.com/datasets/robertusbagaskara/indonesian-food-image) and merge it
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

For Deep learning we use 6 Architectures which are:"
  - Resnet 50 adding classification layer in last
  - Efficient Net with augmentation
  - Efficient Net with added hidden layer in middle 
  - Efficient Net Tuning Without augmentation 
  - Efficient Net Tuning With Aumentation
  - Efficient Net Without Augmentation


<hr>

# Resnet 50 adding classification layer in last
## In graph below you can see that isn't really good to classify this problem, for the first 7 epochs the loss just increasing and the accuracy for validation remain same, so it's not good using this model as a final model.
## <center>Model architecture</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/RESNET50/kesimpulan/arsitektur model.PNG">
</p>

## <center>Model Plot</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/RESNET50/kesimpulan/plot model.png">
</p>

<br>

# Efficient Net with augmentation
## this is the best model we made where the validation accuracy is converged in 79-80% and the training accuracy is 83%, from this plot we can see that the model isn't overfitting because the training accuracy and the validation accuracy gap isn't much than efficient net with augmentation. The model loss start increasing at epoch 5-15 and decresing again.

## <center>Model architecture</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EfficientNetV2LWithAugment/kesimpulan/arsitektur model.PNG">
</p>

## <center>Model Plot</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EfficientNetV2LWithAugment/kesimpulan/plot model.png">
</p>

<br>

# Efficient Net with added hidden layer in middle 
## the model accuracy even decrease than not augment, so adding layer doesnt solve the problem at this moment.

## <center>Model architecture</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EfficientNetV2LWithAugmentDense+/kesimpulan/arsitektur model.PNG">
</p>

## <center>Model Plot</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EfficientNetV2LWithAugmentDense+/kesimpulan/plot model.png">
</p>
<br>

# Efficient Net Tuning Without augmentation 
## after epoch 6 the loss start increasing and the accuracy start being stable in 45% , so it isn's a good model as well
## <center>Model architecture</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EffinetV2L100withoutaug/kesimpulan/arsitektur model.PNG">
</p>

## <center>Model Plot</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EffinetV2L100withoutaug/kesimpulan/plot model.png">
</p>
<br>

# Efficient Net Tuning With Aumentation
## the model at first looks increasing but after epoch 5 to epoch 25 the accuracy just bounce in range 60-70%, so it's not a good model as well because the accuracy doesnt really high
## <center>Model architecture</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EffnetV2L100Augment/kesimpulan/arsitektur model.PNG">
</p>

## <center>Model Plot</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EffnetV2L100Augment/kesimpulan/plot model.png">
</p>
<br>

# Efficient Net Without Augmentation
## sthis is the base model just efficient net and 1 classfication layer without augment or tuning and it turns out after epoch 2 the loss for validation start increasing.

## <center>Model architecture</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EfficientNetV2L/kesimpulan/arsitektur model.PNG">
</p>

## <center>Model Plot</center>
<p align="center">
  <img width="400" height="350" src="https://raw.githubusercontent.com/Bangkit-Team-NutriA/ML/main/Notebook/EfficientNetV2L/kesimpulan/plot model.png">
</p>
<br>

# Conclusion
We took efficient net with augmentation because it's give best accuracy and best val accuracy and also it has converged and the gap between loss in training and validation kind of small so overfitting is avoided in this models.