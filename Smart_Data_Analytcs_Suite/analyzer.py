from base_processor import BaseProcessor
import pandas as pd

class SalesAnalyzer(BaseProcessor):

    def calculate_profit(self):
        self.df["Profit"] = self.df["revenue"] - self.df["cost"]
        self.logger.log("Calculated Profit column")
        return self.df

    def categorize_sales(self):
        # Adaptive quantile-based thresholds
        q25 = self.df["Profit"].quantile(0.25)
        q75 = self.df["Profit"].quantile(0.75)

        def label(x):
            if x >= q75:
                return "High"
            elif x >= q25:
                return "Medium"
            else:
                return "Low"

        self.df["Performance"] = self.df["Profit"].apply(label)

        self.q25 = q25
        self.q75 = q75
        self.mean_profit = self.df["Profit"].mean()
        self.min_profit = self.df["Profit"].min()
        self.max_profit = self.df["Profit"].max()

        self.logger.log(f"3-level categorization -> Low<{q25:.2f}, Medium<{q75:.2f}, High>={q75:.2f}")


        return self.df

    def export_threshold_summary(self, output_path="data/threshold_summary.csv"):
        summary = {
            "Metric": [
                "Profit 25th Percentile (Low Threshold)",
                "Profit 75th Percentile (High Threshold)",
                "Mean Profit",
                "Minimum Profit",
                "Maximum Profit",
                "Total Rows"
            ],
            "Value": [
                round(self.q25, 2),
                round(self.q75, 2),
                round(self.mean_profit, 2),
                round(self.min_profit, 2),
                round(self.max_profit, 2),
                len(self.df)
            ]
        }

        pd.DataFrame(summary).to_csv(output_path, index=False)
        self.logger.log(f"Threshold summary exported to {output_path}")
        return output_path

    def filter_top_performers(self):
        top_df = self.df[self.df["Performance"] == "High"]
        self.logger.log("Filtered top performers (High only)")
        return top_df
