"""
This module contains functions for loading data from database
"""

import pandas as pd
from sqlalchemy import select

from config.config import logger, engine
from database.db_model import RentApartments


def load_data_from_db() -> pd.DataFrame:
    logger.info('Loading data from database')
    query = select(RentApartments)
    return pd.read_sql(query, engine)
