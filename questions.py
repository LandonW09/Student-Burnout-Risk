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
    "stress_rating": NumericQuestion(
        prompt = "On a scale of 0-10, how would you rate your daily stress level?",
        min_val = 0,
        max_val = 10
    ),
    "excercise_minutes": NumericQuestion(
        prompt = "How many minutes of exercise do you get per day? (Max 120 minutes - you may have more, but cap at 120)",
        min_val = 0,
        max_val = 120 #This is a cap to prevent unrealistic answers.
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
    "connection_and_support": ReverseLikertQuestion(
        prompt = "I feel a sense of connection and support from my friends and family.",
    ),
    "help_seeking": ReverseLikertQuestion(
        prompt = "I feel comfortable seeking help from people I trust.",
    ),
    "difficult_times": ReverseLikertQuestion(
        prompt = "When things get difficult, I have people I can turn to for support.",
    ),
    "positive_community": ReverseLikertQuestion(
        prompt = "I feel like I am part of a positive community.",
    ),
    "stress_management": ReverseLikertQuestion(
        prompt = "I manage my stress in a healthy way.",
    ),
    "average_mood": ReverseLikertQuestion(
        prompt = "I feel like I spend more time in a good or neutral mood than a bad mood.",
    ),
    "overcoming_adversity": ReverseLikertQuestion(
        prompt = "When I face adversity, I am confident in my ability to overcome it.",
    ),
    "work_pride": ReverseLikertQuestion(
        prompt = "I take pride in my work and my ability to succeed.",
    ),
    "challenge_seeking": ReverseLikertQuestion(
        prompt = "I seek challenges so that I can push myself to grow and succeed.",
    ),
}
likert_questions = {
    "problem_avoidance": LikertQuestion(
        prompt = "I avoid problems and challenges whenever possible.",
    ),
    "critical_mindset": LikertQuestion(
        prompt = "I am often very critical of myself and others.",
    ),
    "social_withdrawal": LikertQuestion(
        prompt = "When things get difficult, I tend to withdraw from social interactions and activities.",
    ),
    "thought_suppression": LikertQuestion(
        prompt = "I don't usually feel comfortable expressing my feelings and thoughts to others.",
    ),
    "passive_coping": LikertQuestion(
        prompt = "When I am stressed, I cope by distracting myself with passive activities (e.g., scrolling through social media, binge watching TV, etc.)"
    ),
    "workload_overwhelm": LikertQuestion(
        prompt = "I often feel overwhelmed by my workload and responsibilities.",
    ),
    "efficacy_dissatisfaction": LikertQuestion(
        prompt = "I am often dissastisfied with my grades, even when I do well."
    ),
    "perfectionism": LikertQuestion(
        prompt = "I often feel like I need to be perfect in order to succeed, and I am disappointed when I don't meet that standard."
    ),
    "pessimistic_outlook": LikertQuestion(
        prompt = "I often have difficulties maintaining a positive outlook when I have a lot on my plate."
    ),
    "self_soubt": LikertQuestion(
        prompt = "It's hard to believe that I can succeed when I have a lot of work to do."
    )
}