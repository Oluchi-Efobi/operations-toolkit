import pandas as pd

class MemberSatisfactionTracker:
    def __init__(self, feedback_data_path):
        self.feedback_data = pd.read_csv(feedback_data_path)

    def collect_feedback(self, member_id, rating, comments, date=None):
        """Collect feedback from a member."""
        if date is None:
            date = pd.Timestamp.now().strftime("%Y-%m-%d")
        new_feedback = pd.DataFrame({
            "member_id": [member_id],
            "rating": [rating],
            "comments": [comments],
            "date": [date]
        })
        self.feedback_data = pd.concat([self.feedback_data, new_feedback], ignore_index=True)
        self.feedback_data.to_csv(feedback_data_path, index=False)
        return new_feedback.to_dict('records')[0]

    def analyze_satisfaction(self):
        """Analyze satisfaction trends."""
        avg_rating = self.feedback_data['rating'].mean()
        rating_distribution = self.feedback_data['rating'].value_counts().to_dict()
        top_comments = self.feedback_data['comments'].mode().tolist()
        return {
            "average_rating": avg_rating,
            "rating_distribution": rating_distribution,
            "top_comments": top_comments
        }

# Example usage
if __name__ == "__main__":
    tracker = MemberSatisfactionTracker("data/member_feedback.csv")
    feedback = tracker.collect_feedback(
        member_id="M004",
        rating=4,
        comments="More classes needed!"
    )
    print(f"Feedback collected: {feedback}")

    satisfaction_analysis = tracker.analyze_satisfaction()
    print(f"Satisfaction analysis: {satisfaction_analysis}")
