import pandas as pd
import matplotlib.pyplot as plt

class OperationsOptimizer:
    def __init__(self, gym_usage_data_path):
        self.data = pd.read_csv(gym_usage_data_path)

    def analyze_peak_hours(self):
        """Identify peak hours based on gym usage data."""
        peak_hours = self.data.groupby('hour')['usage_count'].sum().idxmax()
        return f"{peak_hours}:00 - {int(peak_hours) + 1}:00"

    def optimize_facility_usage(self):
        """Optimize facility usage by identifying underutilized times."""
        usage_by_facility = self.data.groupby('facility')['usage_count'].mean().sort_values(ascending=False)
        return usage_by_facility.to_dict()

    def plot_usage_trends(self):
        """Plot usage trends over time."""
        plt.figure(figsize=(10, 6))
        for facility in self.data['facility'].unique():
            facility_data = self.data[self.data['facility'] == facility]
            plt.plot(facility_data['hour'], facility_data['usage_count'], label=facility)
        plt.title("Gym Facility Usage Trends")
        plt.xlabel("Hour of the Day")
        plt.ylabel("Usage Count")
        plt.legend()
        plt.grid(True)
        plt.savefig("usage_trends.png")
        plt.close()
        return "usage_trends.png"

# Example usage
if __name__ == "__main__":
    optimizer = OperationsOptimizer("data/gym_usage_data.csv")
    peak_hours = optimizer.analyze_peak_hours()
    print(f"Peak hours: {peak_hours}")

    usage_plan = optimizer.optimize_facility_usage()
    print(f"Optimized facility usage: {usage_plan}")

    plot = optimizer.plot_usage_trends()
    print(f"Usage trends plot saved as: {plot}")
