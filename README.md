# Operations Toolkit

**A Python-based toolkit for optimizing gym operations, staff scheduling, and member satisfaction.**

- **Overseeing daily gym operations** to enhance member satisfaction and streamline service delivery.
- **Managing staff schedules** for a team of 30 members.
- **Ensuring facility organization** and a seamless member experience.

---

##  **Purpose**

This toolkit aims to:  
✅ **Optimize gym operations** (e.g., peak hours, facility usage).  
✅ **Automate staff scheduling** to ensure coverage and balance workloads.  
✅ **Track member satisfaction** and identify areas for improvement.  
✅ **Streamline service delivery** for a better member experience.

---

##  **Features**


| **Module**                    | **Description**                                                               | **Key Functions**                                           |
| ----------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------- |
| `operations_optimizer`        | Optimizes gym operations (e.g., peak hours, facility usage).                  | `analyze_peak_hours()`, `optimize_facility_usage()`         |
| `staff_scheduler`             | Automates staff scheduling for 30+ team members.                              | `generate_schedule()`, `balance_workload()`                 |
| `member_satisfaction_tracker` | Tracks member feedback and satisfaction metrics.                              | `collect_feedback()`, `analyze_satisfaction()`              |
| `service_delivery`            | Streamlines service delivery (e.g., check-ins, equipment maintenance).        | `track_service_times()`, `optimize_service_flow()`          |
| `report_generator`            | Generates reports for operations, staff performance, and member satisfaction. | `generate_operations_report()`, `compile_member_feedback()` |


---

##  **Repository Structure**

```
gym-operations-toolkit/
│   ├── operations_optimizer.py    # Gym operations optimization
│   ├── staff_scheduler.py          # Staff scheduling tool
│   ├── member_satisfaction_tracker.py # Member satisfaction tracking
│   ├── service_delivery.py         # Service delivery optimization
│   └── report_generator.py         # Automated report generation
├── README.md                      # Project documentation
├── requirements.txt                # Python dependencies
└── LICENSE                         # MIT License
```

---

##  **Installation**

### **Prerequisites**

- Python 3.8+
- Required libraries: `pandas`, `numpy`, `matplotlib`, `openpyxl`

### **Setup**

1. Clone the repository:
  ```bash
   git clone https://github.com/Oluchi-Efobi/gym-operations-toolkit.git
   cd operations-toolkit
  ```
2. Install dependencies:
  ```bash
   pip install -r requirements.txt
  ```

---

##  **Quick Start**

### **1. Operations Optimizer**

Analyze peak hours and optimize facility usage:

```python
from scripts.operations_optimizer import OperationsOptimizer

optimizer = OperationsOptimizer("data/gym_usage_data.csv")

# Analyze peak hours
peak_hours = optimizer.analyze_peak_hours()
print(f"Peak hours: {peak_hours}")

# Optimize facility usage
usage_plan = optimizer.optimize_facility_usage()
print(f"Optimized facility usage: {usage_plan}")
```

### **2. Staff Scheduler**

Generate and balance staff schedules:

```python
from scripts.staff_scheduler import StaffScheduler

scheduler = StaffScheduler("data/staff_data.csv")

# Generate a weekly schedule
schedule = scheduler.generate_schedule(
    start_date="2026-06-01",
    end_date="2026-06-07"
)
print(f"Weekly schedule: {schedule}")

# Balance workload among staff
balanced_schedule = scheduler.balance_workload(schedule)
print(f"Balanced schedule: {balanced_schedule}")
```

### **3. Member Satisfaction Tracker**

Collect and analyze member feedback:

```python
from scripts.member_satisfaction_tracker import MemberSatisfactionTracker

tracker = MemberSatisfactionTracker("data/member_feedback.csv")

# Collect feedback from members
feedback = tracker.collect_feedback(
    member_id="M001",
    rating=5,
    comments="Great service and clean facilities!"
)
print(f"Feedback collected: {feedback}")

# Analyze satisfaction trends
satisfaction_analysis = tracker.analyze_satisfaction()
print(f"Satisfaction analysis: {satisfaction_analysis}")
```

### **4. Service Delivery**

Track and optimize service delivery:

```python
from scripts.service_delivery import ServiceDelivery

delivery = ServiceDelivery("data/service_logs.csv")

# Track service times (e.g., check-ins)
service_times = delivery.track_service_times(
    service="check_in",
    start_time="08:00",
    end_time="10:00"
)
print(f"Service times: {service_times}")

# Optimize service flow
optimized_flow = delivery.optimize_service_flow()
print(f"Optimized service flow: {optimized_flow}")
```

### **5. Report Generator**

Generate reports for operations and member satisfaction:

```python
from scripts.report_generator import ReportGenerator

generator = ReportGenerator()

# Generate an operations report
operations_report = generator.generate_operations_report(
    period="May 2026",
    peak_hours=["08:00-10:00", "16:00-18:00"],
    facility_usage={"Treadmills": 90, "Weights": 85}
)
print(operations_report)

# Compile member feedback
feedback_report = generator.compile_member_feedback(
    period="May 2026",
    average_rating=4.5,
    top_feedback=["Clean facilities", "Friendly staff"]
)
print(feedback_report)
```

---

##  **Example Data**

### `**data/gym_usage_data.csv**`

```csv
date,hour,facility,usage_count
2026-05-01,08,Cardio,50
2026-05-01,09,Cardio,75
2026-05-01,10,Cardio,60
2026-05-01,16,Weights,80
```

### `**data/staff_data.csv**`

```csv
staff_id,name,role,availability
001,John Doe,Manager,Full-Time
002,Jane Smith,Trainer,Part-Time
003,Mike Johnson,Receptionist,Full-Time
```

### `**data/member_feedback.csv**`

```csv
member_id,rating,comments,date
M001,5,"Great service!",2026-05-01
M002,4,"Needs more equipment.",2026-05-02
M003,5,"Very clean and organized.",2026-05-03
```

### `**data/service_logs.csv**`

```csv
service,start_time,end_time,duration_minutes
check_in,08:00,08:05,5
check_in,08:05,08:10,5
check_in,08:10,08:20,10
```

---

## 📈 **Use Cases**


| **Scenario**                 | **Tool**                         | **Output**                   |
| ---------------------------- | -------------------------------- | ---------------------------- |
| Analyze peak gym hours       | `operations_optimizer.py`        | Peak hours (list)            |
| Generate staff schedule      | `staff_scheduler.py`             | Weekly schedule (DataFrame)  |
| Collect member feedback      | `member_satisfaction_tracker.py` | Feedback log (CSV)           |
| Track check-in service times | `service_delivery.py`            | Service times (DataFrame)    |
| Generate operations report   | `report_generator.py`            | Operations report (Markdown) |


---

##  **Customization**

### **Extend the Toolkit**

- **Add more facilities**: Update `gym_usage_data.csv` with additional gym equipment.
- **Integrate with gym management software**: Use APIs to fetch live data.
- **Add predictive analytics**: Use `scikit-learn` to forecast member attendance.
- **Automate notifications**: Use `smtplib` to send alerts for low satisfaction scores.

### **Visualization (Optional)**

Add a **Streamlit dashboard** to visualize:

- **Peak hours** and facility usage trends.
- **Staff workload** distribution.
- **Member satisfaction** trends.

Example:

```python
# Install Streamlit: pip install streamlit
import streamlit as st
import pandas as pd

st.title("Gym Operations Dashboard")
df = pd.read_csv("data/gym_usage_data.csv")
st.line_chart(df, x="hour", y="usage_count", color="facility")
```

---

##  **License**

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
