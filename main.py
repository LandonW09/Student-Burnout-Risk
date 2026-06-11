from questions import numeric_questions, reverse_likert_questions, likert_questions
from scoring import score_numeric, score_reverse_likert, score_likert, combine_scores, get_risk_level

def main():
    print("Welcome to the Student Burnout Risk Assessment!")
    print("Please answer the following questions honestly to the best of your ability. It will be most effective if you give accurate answers based on your experiences.")

    #Step 1: Ask questions and collect answers.
    numeric_answers = {key: q.ask() for key, q in numeric_questions.items()}
    reverse_likert_answers = {key: q.ask() for key, q in reverse_likert_questions.items()}
    likert_answers = {key: q.ask() for key, q in likert_questions.items()}

    #Step 2: Score the answers.
    numeric_scores = score_numeric(numeric_answers)
    reverse_likert_scores = score_reverse_likert(reverse_likert_answers)
    likert_scores = score_likert(likert_answers)

    #Step 3: Combine and calculate overall risk.
    percentage_score = combine_scores(numeric_scores, reverse_likert_scores, likert_scores)
    risk_level = get_risk_level(percentage_score)

    #Step 4: Display results.
    print(f"\nYour burnout risk percentage is: {percentage_score}%")
    print(f"Risk Level: {risk_level}")

if __name__ == "__main__":
    main()