"""
This module contains the functions
to build, train, evaluate and save the model.
"""

import pickle as pk
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from config.config import settings, logger
from models.pipeline.preparation import prepare_data


def build_model() -> None:
    logger.info('Building the model')

    # load preprocessed data set
    data = prepare_data()

    # identify X and y
    X, y = _get_x_y(data)

    # split the dataset
    logger.info('Splitting the dataset into test and train sets')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # train the model
    model = _train_model(X_train, y_train)

    # evaluate the model
    _evaluate_model(model, X_test, y_test)

    # save the model in a configuration file
    _save_model(model)


def _get_x_y(
    data: pd.DataFrame,
    col_X: list[str] = [
        'area',
        'constraction_year',
        'bedrooms',
        'garden',
        'balcony_yes',
        'parking_yes',
        'furnished_yes',
        'garage_yes',
        'storage_yes'
    ],
    col_y: str = 'rent'
) -> tuple[pd.DataFrame, pd.Series]:

    logger.info(f'Identifying X and y columns: {col_X}, {col_y}')

    return data[col_X], data[col_y]


def _train_model(
    X_train: pd.DataFrame,
    y_train: pd.Series
) -> RandomForestRegressor:
    logger.info('Training the model with hyperparameters')

    grid_space = {'n_estimators': [100, 200, 300], 'max_depth': [3, 6, 9, 12]}

    logger.debug = f'Hyperparameters grid: {grid_space}'

    grid = GridSearchCV(
        RandomForestRegressor(),
        param_grid=grid_space,
        cv=5,
        scoring='r2',
    )

    model_grid = grid.fit(X_train, y_train)
    return model_grid.best_estimator_


def _evaluate_model(
    model: RandomForestRegressor,
    X_test: pd.DataFrame,
    y_test: pd.Series
) -> float:
    score = model.score(X_test, y_test)
    logger.info(f'Evaluating the model performance. Score: {score}')
    return score


def _save_model(model) -> None:
    path = f'{settings.model_path}/{settings.model_name}'
    logger.info(f'Saving the model in {path}')

    pk.dump(model, open(path, 'wb'))
