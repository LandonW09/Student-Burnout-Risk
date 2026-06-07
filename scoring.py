def score_numeric(answers: dict) -> dict:
    scores = {}
    scores["sleep_hours"] = 12 - answers["sleep_hours"] #Reverse logic.
    scores["feeling_well_rested"] = 7 - answers["feeling_well_rested"] #Reverse logic.
    scores["stress_rating"] = answers["stress_rating"] #No reversal needed.
    scores["exercise_minutes"] = 120 - answers["exercise_minutes"] #Reverse logic.
    scores["missed_obligations"] = answers["missed_obligations"] #No reversal needed.
    scores["days_since_break"] = answers["days_since_break"] #No reversal needed.
    scores["social_interactions"] = 7 - answers["social_interactions"] #Reverse logic.
    return scores
def score_reverse_likert(answers: dict) -> dict: #Reversal already handled in the question class.
    scores = {}
    scores["teacher_relationship"] = answers["teacher_relationship"]
    scores["peer_relationship"] = answers["peer_relationship"]
    scores["school_satisfaction"] = answers["school_satisfaction"]
    scores["perceived_respect"] = answers["perceived_respect"]
    scores["connection_and_support"] = answers["connection_and_support"]
    scores["help_seeking"] = answers["help_seeking"]
    scores["difficult_times"] = answers["difficult_times"]
    scores["positive_community"] = answers["positive_community"]
    scores["stress_management"] = answers["stress_management"]
    scores["average_mood"] = answers["average_mood"]
    scores["overcoming_adversity"] = answers["overcoming_adversity"]
    scores["work_pride"] = answers["work_pride"]
    scores["challenge_seeking"] = answers["challenge_seeking"]
    return scores
def score_likert(answers: dict) -> dict: #No reversal needed for these questions.
    scores = {}
    scores["problem_avoidance"] = answers["problem_avoidance"]
    scores["critical_mindset"] = answers["critical_mindset"]
    scores["social_withdrawal"] = answers["social_withdrawal"]
    scores["thought_suppression"] = answers["thought_suppression"]
    scores["passive_coping"] = answers["passive_coping"]
    scores["workload_overwhelm"] = answers["workload_overwhelm"]
    scores["efficacy_dissatisfaction"] = answers["efficacy_dissatisfaction"]
    scores["perfectionism"] = answers["perfectionism"]
    scores["pessimistic_outlook"] = answers["pessimistic_outlook"]
    scores["self_doubt"] = answers["self_doubt"]
    return scores