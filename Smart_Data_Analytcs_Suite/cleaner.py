from base_processor import BaseProcessor
import pandas as pd

class Cleaner(BaseProcessor):
    def clean_columns(self):
        self.df.columns = self.df.columns.map(lambda x: x.strip().lower().replace(" ","_"))
        self.logger.log('Cleaned column names')
        return self.df
    
    def fill_missing_values(self):
        self.df = self.df.applymap(lambda x: 0 if pd.isna(x) else x)
        self.logger.log("Filled missimg values")
        return self.df
    
    