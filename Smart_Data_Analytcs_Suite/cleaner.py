from base_processor import BaseProcessor
import pandas as pd

class Cleaner(BaseProcessor):
    def clean_columns(self):
        self.df.columns = self.df.columns.map(lambda x: x.strip().lower().replace(" ","_"))
        self.logger.log('Cleaned column names')
        return self.df
    
    def fill_missing_values(self):
        self.df = self.df.applymap(lambda x: 0 if pd.isna(x) else x)
        self.logger.log("Filled missing values")
        return self.df
    
    def filter_invalid_rows(self):
        valid_rows = filter(
            lambda row: row["sales"] >= 0 and row["revenue"] >= 0,
            self.df.to_dict("records")
        )
        self.df = pd.DataFrame(list(valid_rows))
        self.logger.log("Filtered invalid rows (sales < 0 or revenue < 0)")
        return self.df
