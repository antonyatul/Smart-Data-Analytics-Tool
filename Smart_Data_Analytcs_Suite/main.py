from cleaner import Cleaner
from analyzer import SalesAnalyzer
from visualizer import Visualizer

def main():
    input_file = r"C:\Users\alvia\Documents\Luminar\Smart Data Analytics Tool\Smart_Data_Analytcs_Suite\Data\sales_data.csv"
    cleaned_output = "data/cleaned_sales.csv"
    analysis_output = "data/top_performers.csv"

    #Data Cleaning
    cleaner = Cleaner(input_file)
    cleaner.load_data()
    cleaner.clean_columns()
    cleaner.fill_missing_values()
    cleaner.filter_invalid_rows()
    cleaner.save_to_csv(cleaned_output)

    #Data analysis
    analyzer = SalesAnalyzer(cleaned_output)
    analyzer.load_data
    analyzer.calculate_profit()
    analyzer.categorize_sales()
    top_df = analyzer.filter_top_performers()
    analyzer.logger.log(f'Saved Top performers to {analysis_output}')

    #Visualization
    viz = Visualizer()
    viz.plot_sales_vs_profit(analyzer.df)

    print('\n Smart Data Analytics Suite completed successfully!')

if __name__ == "__main__":
    main()