import matplotlib.pyplot as plt
from logger import Logger

class Visualizer:
    def __init__(self):
        self.logger = Logger("logs.txt")

    def plot_sales_vs_profit(self, df):
        plt.figure(figsize=(8, 5))
        plt.scatter(df["sales"], df["Profit"])
        plt.title("Sales vs Profit", fontsize=14)
        plt.xlabel("Sales")
        plt.ylabel("Profit")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("data/sales_vs_profit.png")
        self.logger.log("Generated Sales vs Profit graph (saved to data/sales_vs_profit.png)")
        print("📈 Graph generated: data/sales_vs_profit.png")
