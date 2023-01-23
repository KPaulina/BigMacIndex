import pandas as pd
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))[:-3]
DATA_DIR = os.path.join(BASE_DIR, 'data')


def countries_full_name_for_top_5(df: pd.DataFrame) -> pd.DataFrame:
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


def load_big_mac_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    df_big_mac = pd.read_excel(os.path.join(DATA_DIR, 'big_mac_data.xlsx'))
    df_big_mac = df_big_mac.sort_values(by='dollar_price', ascending=False)
    df_top_five_big_macs = df_big_mac.iloc[:5]
    df_top_five_big_macs = countries_full_name_for_top_5(df_top_five_big_macs)
    return df_top_five_big_macs, df_big_mac
