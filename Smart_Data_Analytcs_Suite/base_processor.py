import pandas as pd
from logger import Logger

class BaseProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.logger = Logger("logs.txt")

    def load_data(self):
        if self.file_path.endswith(".csv"):
            self.df = pd.read_csv(self.file_path)
        elif self.file_path.endswith(".xlsx") or self.file_path.endswith(".xls"):
            self.df = pd.read_excel(self.file_path)
        else:
            raise ValueError("Unsupported file format. Please use CSV or Excel.")
        
        self.logger.log(f"Loaded data from {self.file_path}")
        return self.df

    
    def save_to_csv(self, output_path):
        self.df.to_csv(output_path, index=False)
        self.logger.log(f'Saved CSV to {output_path}')

    def show_summary(self):
        self.logger.log("Display data sumamary")
        print('Data Summary')
        print(self.df.describe())
