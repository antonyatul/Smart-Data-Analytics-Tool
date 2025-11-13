import matplotlib.pyplot as plt

class Visualizer:

    def plot_sales_vs_profit(self, df):
        plt.figure(figsize=(8,5))
        plt.scatter(df["sales"], df["Profit"])
        plt.xlabel("Sales")
        plt.ylabel("Profit")
        plt.title("Sales vs Profit")
        plt.savefig("data/sales_vs_profit.png")
        plt.close()

    def plot_profit_thresholds(self, df, q25, q75, mean_profit):
        plt.figure(figsize=(10,6))

        # Histogram
        plt.hist(df["Profit"], bins=50, alpha=0.7)

        # Vertical lines
        plt.axvline(q25, color="orange", linestyle="--", linewidth=2, label=f"25th Percentile: {q25:.2f}")
        plt.axvline(q75, color="green", linestyle="--", linewidth=2, label=f"75th Percentile: {q75:.2f}")
        plt.axvline(mean_profit, color="red", linestyle="-", linewidth=2, label=f"Mean Profit: {mean_profit:.2f}")

        plt.title("Profit Distribution with Thresholds")
        plt.xlabel("Profit")
        plt.ylabel("Frequency")
        plt.legend()

        plt.savefig("data/profit_thresholds.png")
        plt.close()
