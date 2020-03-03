import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


lowa_dataset_path = '../kaggle_machine_learning/datasets/lowa.csv'
dataframe = pd.read_csv(lowa_dataset_path)
y = dataframe.SalePrice
x = dataframe[['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']]

""""
A simple training model would be to train all the data with features(x)
and result(y). It sounds so simple. But the problem with this approach is
accuracy. Its not the best way to get the results for new data.

If we train the model with all the training data, the result would be perfect for
only the training set and not the new set of data.

"""""

lowa_model_one = DecisionTreeRegressor()
# FitModel
lowa_model_one.fit(x,y)
# In sample score
error_one = mean_absolute_error(y, lowa_model_one.predict(x))
print(error_one)

"""""
one way to train the model is to divide the training data set to two parts.
oen is for training the model and another is for testing.
This will show us the accuracy of the model and also lets us to test with
new data ( second part of training data ). 
"""""

train_x, val_x, train_y, val_y = train_test_split(x,y, random_state=0)
lowa_model_two = DecisionTreeRegressor()
lowa_model_two.fit(train_x, train_y)
error_two = mean_absolute_error(val_y, lowa_model_two.predict(val_x))

print(error_two)

