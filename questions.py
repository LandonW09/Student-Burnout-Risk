class Question:
    def __init__(self, prompt):
        self.prompt = prompt
    def validate(self, answer):
        raise NotImplementedError
class NumericQuestion(Question):
    def __init__(self, prompt, min_val=None, max_val=None):
        super().__init__(prompt)
        self.min_val = min_val
        self.max_val = max_val
class LikertQuestion(Question):
    def __init__(self, prompt, scale=5):
        super().__init__(prompt)
        self.scale = {
            1: "Strongly Disagree",
            2: "Disagree",
            3: "Neutral",
            4: "Agree",
            5: "Strongly Agree"
        }
    
questions = {
    "sleep hours": NumericQuestion(
        prompt = "How many hours of sleep do you get per night?",
        min_val = 0,
        max_val = 24
    ),
    "school satisfaction": LikertQuestion(
        prompt="I am satisfied with my school experience."
    ),
}