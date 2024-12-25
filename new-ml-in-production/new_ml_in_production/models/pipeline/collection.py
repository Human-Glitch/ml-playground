import pandas as pd
from config.config import logger, engine
from database.db_model import RentApartments
from sqlalchemy import select

def load_data_from_db():
    logger.info(f"Loading data from database")
    query = select(RentApartments)
    return pd.read_sql(query, engine)