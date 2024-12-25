import pandas as pd
from config import logger, engine
from db_model import RentApartments
from sqlalchemy import select

def load_data_from_db():
    logger.info(f"Loading data from database")
    query = select(RentApartments)
    return pd.read_sql(query, engine)