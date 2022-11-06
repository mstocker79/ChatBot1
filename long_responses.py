import random

R_EATING = "I can't eat anything because I am a bot!"


def unknown():
    response = ['Could you please re-phrase that?',
                "....",
                "Sounds about right",
                "What does that mean?",
                "Why would you say that?",
                "I wouldn't bet on that."][random.randrange(6)]
    return response