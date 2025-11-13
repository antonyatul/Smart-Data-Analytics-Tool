import os
from cleaner import Cleaner
from analyzer import SalesAnalyzer
from visualizer import Visualizer

def main():

    # 🔥 Auto-create data folder if missing
    if not os.path.exists("data"):
        os.makedirs("data")

    # ✔️ Input CSV inside /data folder
    input_file = r"C:\Users\alvia\Documents\Luminar\Smart Data Analytics Tool\Smart_Data_Analytcs_Suite\raw_data\big_sales_data.csv"

    # ✔️ Output file locations (all inside /data)
    cleaned_output = "data/cleaned_sales.csv"
    analysis_output = "data/top_performers.csv"
    graph_output = "data/sales_vs_profit.png"

    # 🧼 STEP 1 — CLEANING MODULE
    cleaner = Cleaner(input_file)
    cleaner.load_data()
    cleaner.clean_columns()
    cleaner.fill_missing_values()
    cleaner.filter_invalid_rows()
    cleaner.save_to_csv(cleaned_output)

    # 📊 STEP 2 — ANALYZER MODULE
    analyzer = SalesAnalyzer(cleaned_output)
    analyzer.load_data()
    analyzer.calculate_profit()
    analyzer.categorize_sales()
    analyzer.export_threshold_summary("data/threshold_summary.csv")
    top_df = analyzer.filter_top_performers()

    # Save Top Performers CSV
    top_df.to_csv(analysis_output, index=False)
    analyzer.logger.log(f"Saved Top performers to {analysis_output}")

    # 📈 STEP 3 — VISUALIZER MODULE
    viz = Visualizer()
    viz.plot_sales_vs_profit(analyzer.df)

    print("\n✨ Smart Data Analytics Suite completed successfully! ✨")
    print("✔ Cleaned file saved to:", cleaned_output)
    print("✔ Top performers saved to:", analysis_output)
    print("✔ Graph saved to:", graph_output)
    print("✔ Logs updated in logs.txt")

    # 🚀 AUTO-OPEN OUTPUT FOLDER
    output_folder = os.path.abspath("data")
    print("\n📂 Opening output folder:", output_folder)
    os.startfile(output_folder)

    # # 🚀 OPTIONAL: Auto-open cleaned CSV
    # print("📄 Opening cleaned CSV...")
    # os.startfile(os.path.abspath(cleaned_output))

    # # 🚀 OPTIONAL: Auto-open graph
    # print("📊 Opening graph...")
    # os.startfile(os.path.abspath(graph_output))


if __name__ == "__main__":
    main()
