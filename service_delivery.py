import pandas as pd

class ServiceDelivery:
    def __init__(self, service_logs_path):
        self.service_logs = pd.read_csv(service_logs_path)

    def track_service_times(self, service, start_time, end_time):
        """Track service times for a specific service."""
        filtered_logs = self.service_logs[
            (self.service_logs['service'] == service) &
            (self.service_logs['start_time'] >= start_time) &
            (self.service_logs['end_time'] <= end_time)
        ]
        return filtered_logs

    def optimize_service_flow(self):
        """Optimize service flow by identifying bottlenecks."""
        avg_times = self.service_logs.groupby('service')['duration_minutes'].mean().to_dict()
        bottlenecks = {service: time for service, time in avg_times.items() if time > 10}  # Threshold: 10 minutes
        return {
            "average_times": avg_times,
            "bottlenecks": bottlenecks
        }

# Example usage
if __name__ == "__main__":
    delivery = ServiceDelivery("data/service_logs.csv")
    service_times = delivery.track_service_times(
        service="check_in",
        start_time="08:00",
        end_time="10:00"
    )
    print(f"Service times for check-ins:\n{service_times}")

    optimized_flow = delivery.optimize_service_flow()
    print(f"Optimized service flow: {optimized_flow}")
