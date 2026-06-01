import pandas as pd
from datetime import datetime, timedelta
import random

class StaffScheduler:
    def __init__(self, staff_data_path):
        self.staff_data = pd.read_csv(staff_data_path)

    def generate_schedule(self, start_date, end_date):
        """Generate a weekly schedule for staff."""
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        delta = end - start
        days = [start + timedelta(days=i) for i in range(delta.days + 1)]

        schedule = []
        for day in days:
            day_str = day.strftime("%Y-%m-%d")
            for _, staff in self.staff_data.iterrows():
                if staff["availability"] == "Full-Time":
                    shift = random.choice(["Morning", "Afternoon", "Evening"])
                else:
                    shift = random.choice(["Morning", "Afternoon"])
                schedule.append({
                    "date": day_str,
                    "staff_id": staff["staff_id"],
                    "name": staff["name"],
                    "shift": shift
                })
        return pd.DataFrame(schedule)

    def balance_workload(self, schedule_df):
        """Balance workload by ensuring even distribution of shifts."""
        shift_counts = schedule_df.groupby(['staff_id', 'name'])['shift'].value_counts().unstack(fill_value=0)
        balanced_schedule = []
        for _, row in shift_counts.iterrows():
            staff_id = row.name
            name = row.index[1] if isinstance(row.index, tuple) else row.name
            for shift in ["Morning", "Afternoon", "Evening"]:
                if row.get(shift, 0) < 2:  # Ensure no more than 2 shifts of the same type per week
                    balanced_schedule.append({
                        "staff_id": staff_id,
                        "name": name,
                        "shift": shift,
                        "count": row.get(shift, 0)
                    })
        return pd.DataFrame(balanced_schedule)

# Example usage
if __name__ == "__main__":
    scheduler = StaffScheduler("data/staff_data.csv")
    schedule = scheduler.generate_schedule(start_date="2026-06-01", end_date="2026-06-07")
    print("Generated schedule:\n", schedule.head())

    balanced_schedule = scheduler.balance_workload(schedule)
    print("Balanced schedule:\n", balanced_schedule)
