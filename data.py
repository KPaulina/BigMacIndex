import pandas as pd
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def add_full_names_of_countries_in_top_5(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Function created to create column that has names of the top 5 countries
    :param df:
    :return:
    '''
    condition = [
        df['country_code'] == "VEN",
        df['country_code'] == "CHE",
        df['country_code'] == "NOR",
        df['country_code'] == "SWE",
        df['country_code'] == "USA"
    ]
    choices = [
        'Venezuela', 'Switzerland', 'Norway',
        'Sweden', 'United States'
    ]
    df['countries'] = np.select(condition, choices)
    return df


def load_big_mac_data() -> pd.DataFrame:
    '''
    Function created to load data about big mac index from excel
    :return:
    '''
    return pd.read_excel(os.path.join(BASE_DIR, 'big_mac_data.xlsx'))


def sort_by_the_highest_value(df_big_mac: pd.DataFrame) -> pd.DataFrame:
    '''
    Function that sorts by dollar price value from the highest value to the lowest
    :param df_big_mac:
    :return:
    '''
    return df_big_mac.sort_values(by='dollar_price', ascending=False)


def get_top_5_countries_with_highest_big_mac_index(df_big_mac: pd.DataFrame) -> pd.DataFrame:
    '''
    Function that gets top 5 countries with the highest big mac index
    :param df_big_mac:
    :return:
    '''
    df_top_five_big_macs = df_big_mac.iloc[:5].copy()
    return add_full_names_of_countries_in_top_5(df_top_five_big_macs)

