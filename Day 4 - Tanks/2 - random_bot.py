import random

def make_choice(x,y,field):
    return random.choice([
        "go_right", "go_left",
        "go_down", "go_up"
    ])
