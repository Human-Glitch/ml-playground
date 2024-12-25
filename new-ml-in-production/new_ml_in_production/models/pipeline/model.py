from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from models.pipeline.preparation import prepare_data
from sklearn.model_selection import GridSearchCV
import pickle as pk
from config.config import settings, logger

def build_model():
    logger.info("Building the model")

    # load preprocessed data set
    data = prepare_data()

    # identify X and y
    X, y = get_X_y(data)

    # split the dataset
    logger.info("Splitting the dataset into test and train sets")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # train the model
    model = train_model(X_train, y_train)

    # evaluate the model
    evaluate_model(model, X_test, y_test)

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
    
    logger.info(f"Identifying X and y columns: {col_X}, {col_y}")
     
    return data[col_X], data[col_y]

def train_model(X_train, y_train):
    logger.info("Training the model with hyperparameters")
    
    grid_space = {'n_estimators': [100, 200, 300], 'max_depth': [3, 6, 9, 12]}
    
    logger.debug = f"Hyperparameters grid: {grid_space}"
    
    grid = GridSearchCV(RandomForestRegressor(), param_grid=grid_space, cv=5, scoring = 'r2')
    model_grid = grid.fit(X_train, y_train)

    return model_grid.best_estimator_

def evaluate_model(model, X_test, y_test):
    score = model.score(X_test, y_test)
    logger.info(f"Evaluating the model performance. Score: {score}")
    return score
    
def save_model(model):
    path = f'{settings.model_path}/{settings.model_name}'
    logger.info(f"Saving the model in {path}")
    
    pk.dump(model, open(path, 'wb'))

