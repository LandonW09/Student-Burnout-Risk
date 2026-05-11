credit_hours = int(input('Enter your current credit hours: '))
nightly_sleep_hours = int(input('Enter your nightly sleep hours: '))
daily_stress_rating = int(input('Enter your daily stress rating (0-10): '))
daily_exercise_minutes = int(input('Enter your daily exercise minutes: '))

risk_config = { #Dictionary to hold all risk variables, thresholds, and label for the final print statement.
    'credit_hours': {
        'input value': credit_hours,
        'thresholds': [(18, 5), (15, 3), (12, 2), (9, 1)], #Tentative thresholds while I work out exact values for each risk factor.
        'label': 'Credit Hours Risk: '
    },
    'sleep': {
        'input value': nightly_sleep_hours,
        'thresholds': [(9, 1), (7, 2), (6, 3), (5, 4), (4, 5)],
        'label': 'Sleep Risk: '
    },
    'stress': {
        'input value': daily_stress_rating,
        'thresholds': [(8, 5), (6, 4), (4, 3), (3, 2), (0, 1)],
        'label': 'Stress Risk: '
    },
    'exercise_minutes': {
        'input value': daily_exercise_minutes,
        'thresholds': [(45, 1), (35, 2), (25, 3), (15,4), (0,5)],
        'label': 'Exercise Risk: '
    }
}

def assess_risk(input_value, thresholds): #Uses the risk_config dictionary.
    for threshold, risk in thresholds:
        if input_value >= threshold:
            return risk
scores = [] #List to hold all risk scores for final calculation.
for key, config in risk_config.items():
    risk = config['input value']
    thresholds = config['thresholds']
    score = assess_risk(risk, thresholds) #Variable used in the final calculation of burnout risk percentage.
    scores.append(score)
    print(f'{config['label']}{score}/5')

def assess_overall_risk(scores):
    max_score = len(scores) * 5 #Maximum possible score based on maximum risk value.
    return round((sum(scores)/max_score) * 100)

print(f'Overall Burnout Risk: {assess_overall_risk(scores)}%')