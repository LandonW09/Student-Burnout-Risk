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
    def ask(self):
        while True:
            try:
                answer = float(input(self.prompt + " ")) #input(self.prompt) + " " prints question and waits for answer. Float converts answer to number.
                if self.validate(answer):
                    return answer
                else:
                    print(f"Please enter a number between {self.min_val} and {self.max_val}.")
            except ValueError: #This is if user enters something other than a number.
                print("Please enter a valid number within the given range.")

class LikertQuestion(Question):
    def __init__(self, prompt, scale=5):
        super().__init__(prompt)
        self.scale = { #The user will answer with a number 1 through 5. Labels show what each number means.
            1: "Strongly Disagree",
            2: "Disagree",
            3: "Neutral",
            4: "Agree",
            5: "Strongly Agree"
        }
    def score_response(self, answer): #This is a placeholder method meant to be overridden by ReverseLikertQuestion subclass.
        return answer
    def ask(self):
        while True:
            print(self.prompt)
            for num, label in self.scale.items(): #Prints each option in the Likert scale for each question.
                print(f"{num}. {label}")
            try:
                answer = int(input("Enter your response (1-5): ")) 
                if 1 <= answer <= 5: #Makes sure answer is between 1 and 5.
                    return self.score_response(answer)
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number within the given range.")

class ReverseLikertQuestion(LikertQuestion):
    def score_response(self, answer):
        return 6 - answer #Reverses the score so that higher scores indicate lower risk.

numeric_questions = { #These questions prompt simple numeric answers. They will later need thresholds and validation.
    "sleep_hours": NumericQuestion(
        prompt = "How many hours of sleep do you get per night? Try to estimate an answer between 0-9.",
        min_val = 0,
        max_val = 9
    ),
    "feeling_well_rested": NumericQuestion(
        prompt = "How many days a week do you feel well-rested when you wake up? Try to estimate an answer between 0-7.",
        min_val = 0,
        max_val = 7
    ),
    "stress_rating": NumericQuestion(
        prompt = "On a scale of 0-10, how would you rate your daily stress level?",
        min_val = 0,
        max_val = 10
    ),
    "exercise_minutes": NumericQuestion(
        prompt = "How many minutes of exercise do you get per week? Try to estimate an answer between 0-300.",
        min_val = 0,
        max_val = 300 #Many reccomendations suggest that 300 minutes per week is ideal.
    ),
    "missed_obligations": NumericQuestion(
        prompt = "In the past week, how many times have you missed class or other obligations due to poor mental health? Try to estimate an answer 0-20.",
        min_val = 0,
        max_val = 20 #There isn't an exact healthy range, but missing this many obligations is a likely sign of burnout.
    ),
    "days_since_break": NumericQuestion(
        prompt = "How many days has it been since you had a full day without academic responsibilities (e.g., no classes, homework, studying, etc.)? Try to estimate an answer 0-30.",
        min_val = 0,
        max_val = 30 #A healthy range is at least 1 day a week, so 30 is a reasonable max.
    ),
    "social_interactions": NumericQuestion(
        prompt = "On average, how many days a week do you have meaningful social interactions with friends or family? Try to estimate an answer between 0-7.",
        min_val = 0,
        max_val = 7
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
    "self_doubt": LikertQuestion(
        prompt = "It's hard to believe that I can succeed when I have a lot of work to do."
    )
}