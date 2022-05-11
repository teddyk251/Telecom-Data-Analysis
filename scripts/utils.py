import pandas as pd
import numpy as np

class Utils:

    def load_data(self, data_path):
        """
        Load data from a csv file.
        """
        try:
            df = pd.read_csv(data_path)
        except FileNotFoundError:
            print("File not found.")
        return df

    def save_data(self, df, data_path):
        """
        Save data to a csv file.
        """
        try:
            df.to_csv(data_path)
        except Exception as e:
            print(f"Saving failed {e}")
    

