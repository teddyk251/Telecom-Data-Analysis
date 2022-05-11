import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, data_path):
        self.df = pd.read_csv(data_path)

    def drop_duplicate(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        drop duplicate rows
        """
        df.drop_duplicates(inplace=True)

        return df

    def convert_to_datetime(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        convert column to datetime
        """

        df[['start','end']] = df[['start','end']].apply(pd.to_datetime)

        return df

    def percent_missing(self, df: pd.DataFrame) -> float:
        """
        calculate the percentage of missing values from dataframe
        """
        totalCells = np.product(df.shape)
        missingCount = df.isnull().sum()
        totalMising = missingCount.sum()

        return round(totalMising / totalCells * 100, 2)

    def percent_missing_column(self, df: pd.DataFrame, col:str) -> float:
        """
        calculate the percentage of missing values for the specified column
        """
        try:
            col_len = len(df[col])
        except KeyError:
            print(f"{col} not found")
        missing_count = df[col].isnull().sum()

        return round(missing_count / col_len * 100, 2)


    
