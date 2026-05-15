class Question:
    def __init__(self, prompt):
        self.prompt = prompt #All questions have this in common.
class NumericQuestion(Question):
    def __init__(self, prompt, min_val=None, max_val=None): #min and max are defined within each key of the numeric dictionary.
        super().__init__(prompt) #This is in every subclass. It runs the __init__ method from the parent class to call prompt.
        self.min_val = min_val
        self.max_val = max_val
    def validate(self, answer):
        if self.min_val is not None and answer < self.min_val:
            return False
        if self.max_val is not None and answer > self.max_val:
            return False
        return True
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
    def score_response(self, answer):
        return answer
class ReverseLikertQuestion(LikertQuestion):
    def score_response(self, answer):
        return 6 - answer #Reverses the score so that higher scores indicate lower risk.

numeric_questions = { #These questions prompt simple numeric answers. They will later need thresholds and validation.
    "sleep_hours": NumericQuestion(
        prompt = "How many hours of sleep do you get per night?",
        min_val = 0,
        max_val = 24
    ),
}
reverse_likert_questions = { #These questions are reversed to align higher scores with lower risk.
    "teacher_relationship": ReverseLikertQuestion(
        prompt = "I have a positive relationship with my teachers.",
    ),
    "peer_relationship": ReverseLikertQuestion(
        prompt = "I have a positive relationship with my peers/classmates.",
    ),
    "school_satisfaction": ReverseLikertQuestion(
        prompt = "I feel satisfied with my overall school experience.",
    ),
    "perceived_respect": ReverseLikertQuestion(
        prompt = "I feel respected by my teachers and peers.",
    ),
}