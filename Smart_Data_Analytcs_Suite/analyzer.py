from base_processor import BaseProcessor
import pandas as pd


class SalesAnalyzer(BaseProcessor):
    def calculate_profit(self):
        self.df["Profit"] = self.df.apply(lambda row: row["revenue"] - row["cost"], axis=1)
        self.logger.log("Calculated profit for all rows")
        return self.df
    
    def categorize_sales(self):
        self.df["performance"] = self.df["sales"].apply(lambda x: "High" if x>1000 else "low")
        self.logger.log("Categorized sales into High/Low")
        return self.df
    
    def filter_top_performers(self):
        top = filter(lambda row: row["performance"] == "High", self.df.to_dict("records"))
        top_df = pd.DataFrame(list(top))
        self.logger.log(f'Filtered {len(top_df)} top-performing records')
        return top_df
    