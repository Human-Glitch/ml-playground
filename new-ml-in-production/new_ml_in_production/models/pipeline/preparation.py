import re
import pandas as pd

from config.config import logger
from models.pipeline.collection import load_data_from_db


def prepare_data() -> pd.DataFrame:
    logger.info('Preparing data')

    # 1. load the data
    data = load_data_from_db()

    # 2. encode the columns
    data_encoded = encode_cat_cols(data)

    # 3. parse the garden column
    df = parse_garden_cols(data_encoded)

    return df


def encode_cat_cols(data: pd.DataFrame) -> pd.DataFrame:
    cols = ['balcony', 'parking', 'furnished', 'garage', 'storage']
    logger.info(f'Encoding columns: {cols}')

    return pd.get_dummies(
        data,
        columns=cols,
        drop_first=True
    )


def parse_garden_cols(data: pd.DataFrame) -> pd.DataFrame:
    logger.info('Parsing garden column')
    for i in range(len(data)):
        if data.garden[i] == 'Not present':
            data.garden[i] = 0
        else:
            data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])

    return data
