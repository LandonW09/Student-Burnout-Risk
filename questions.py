class Question:
    def __init__(self, promt, qtype="float", min_val=None, max_val=None):
        self.prompt = prompt
        self.qtype = qtype
        self.min_val = min_val
        self.max_val = max_val

questions = {
    "sleep hours": Question(
        prompt = "How many hours of sleep do you get per night?",
        min_val = 0,
        max_val = 24
    )
}