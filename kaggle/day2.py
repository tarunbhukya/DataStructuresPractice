import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

lowa_data_set = "../kaggle/datasets/lowa.csv"
dataframe = pd.read_csv(lowa_data_set)
y = dataframe.SalePrice
x = dataframe[['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']]

train_x, val_x, train_y, val_y = train_test_split(x, y, random_state=0)


"""""
when we add less features i.e atleast one then the model would be underfitting
like for example lets say we have vehicles data like 4 wheels, color, etc
and we add features like just 4 wheels and color. and want to know if its a car or not.
with fewer features we cannot really get our answers i.e wether if its a car or not as
we have fewer features trained in the model. This is underfitting.

When we add more features i.e add brand, add structure and some other fields etc. 
and if we train this model and and we want the answers like the brand of the car,
we could surely get the result but, lets say in the test data we have fewer data and
we just wanted to know whether its a car or not the above model might not give
reliable answers as we trained the model with extra features which are not required

branching out more with more and more features would lead to overfitting.
So we have to find the balance between them. so basically we have to controle the 
tree depth, less features etc
"""""


def get_mean_absolute_error(max_leaf_nodes, train_x, train_y, val_x, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_x, train_y)
    predicted_values = model.predict(val_x)
    mae = mean_absolute_error(val_y, predicted_values)
    return mae


# compare mae with different max leaf nodes
def best_tree_size():
    scores = {
        leaf_size: get_mean_absolute_error(leaf_size, train_x, train_y, val_x, val_y)
        for leaf_size in [5, 50, 500, 5000]
    }
    print(scores)
    best_size = min(scores, key=scores.get)
    return best_size

# now train the model with the best fit tree size
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size(), random_state=1)
final_model.fit(x,y)


"""""
DecisionTress are good but there are other good training models 
out there. Lets see whats next :)
"""""



