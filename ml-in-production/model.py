from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from preparation import prepare_data
from sklearn.model_selection import GridSearchCV
import pickle as pk

def build_model():

    # load preprocessed data set
    data = prepare_data()

    # identify X and y
    X, y = get_X_y(data)

    # split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # train the model
    model = train_model(X_train, y_train)

    # evaluate the model
    score = evaluate_model(model, X_test, y_test)
    print(score)

    # save the model in a configuration file
    save_model(model)

def get_X_y(data,
            col_X = ['area', 
                  'constraction_year', 
                  'bedrooms', 
                  'garden', 
                  'balcony_yes', 
                  'parking_yes', 
                  'furnished_yes', 
                  'garage_yes', 
                  'storage_yes'],
            col_y = 'rent'):
     
    return data[col_X], data[col_y]

def train_model(X_train, y_train):
    grid_space = {'n_estimators': [100, 200, 300], 'max_depth': [3, 6, 9, 12]}
    grid = GridSearchCV(RandomForestRegressor(), param_grid=grid_space, cv=5, scoring = 'r2')
    model_grid = grid.fit(X_train, y_train)

    return model_grid.best_estimator_

def evaluate_model(model, X_test, y_test):
   return model.score(X_test, y_test)
    
def save_model(model):
    pk.dump(model, open('models/rf_v1', 'wb'))

rf = build_model()

