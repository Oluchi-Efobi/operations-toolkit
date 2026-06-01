class ReportGenerator:
    def generate_operations_report(self, period, peak_hours, facility_usage):
        """Generate an operations report."""
        report = f"""
        # Gym Operations Report
        **Period:** {period}

        ## Peak Hours
        {', '.join(peak_hours)}

        ## Facility Usage
        """
        for facility, usage in facility_usage.items():
            report += f"- **{facility}**: {usage}% usage\n"
        return report

    def compile_member_feedback(self, period, average_rating, top_feedback):
        """Compile a member feedback report."""
        report = f"""
        # Member Satisfaction Report
        **Period:** {period}

        ## Average Rating
        **{average_rating}/5**

        ## Top Feedback
        """
        for feedback in top_feedback:
            report += f"- {feedback}\n"
        return report

# Example usage
if __name__ == "__main__":
    generator = ReportGenerator()
    operations_report = generator.generate_operations_report(
        period="May 2026",
        peak_hours=["08:00-10:00", "16:00-18:00"],
        facility_usage={"Treadmills": 90, "Weights": 85}
    )
    print(operations_report)

    feedback_report = generator.compile_member_feedback(
        period="May 2026",
        average_rating=4.5,
        top_feedback=["Clean facilities", "Friendly staff"]
    )
    print(feedback_report)
