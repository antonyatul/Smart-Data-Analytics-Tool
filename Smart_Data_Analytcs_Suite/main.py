import os
from cleaner import Cleaner
from analyzer import SalesAnalyzer
from visualizer import Visualizer

def main():

    #  auto-create data folder if missing
    if not os.path.exists("data"):
        os.makedirs("data")

    input_file = r"C:\Users\alvia\Documents\Luminar\Smart Data Analytics Tool\Smart_Data_Analytcs_Suite\Data\sales_data.csv"
    cleaned_output = "data/cleaned_sales.csv"
    analysis_output = "data/top_performers.csv"

    ...
