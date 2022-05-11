import pandas as pd
import numpy as np


class Utils:

    def load_data(self, data_path: str) -> pd.DataFrame:
        """
        Load data from a csv file.
        """
        try:
            df = pd.read_csv(data_path)
        except FileNotFoundError:
            print("File not found.")
        return df

    def save_data(self, df: pd.DataFrame, data_path:str) -> None:
        """
        Save data to a csv file.
        """
        try:
            df.to_csv(data_path)
        except Exception as e:
            print(f"Saving failed {e}")

    def convert_bytes_to_megabytes(self,  bytes_data:float) -> float:

        megabyte = 1*10e+5
        result_mb = bytes_data / megabyte

        return result_mb
