from collection import load_data
import re
import pandas as pd

def prepare_data():
    #1. load the data
    data = load_data()

    #2. encode the columns
    data_encoded = encode_cat_cols(data)

    #3. parse the garden column
    df = parse_garden_cols(data_encoded)

    return df

def encode_cat_cols(data):
    return pd.get_dummies(data, 
                          columns = ['balcony',
                                     'parking', 
                                     'furnished', 
                                     'garage', 
                                     'storage'], 
                          drop_first=True)


def parse_garden_cols(data):
    for i in range(len(data)):
        if data.garden[i] == 'Not present':
            data.garden[i] = 0
        else: data.garden[i] = int(re.findall(r'\d+', data.garden[i])[0])

    return data


df = prepare_data()
print(df)