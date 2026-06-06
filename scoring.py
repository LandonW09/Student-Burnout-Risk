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