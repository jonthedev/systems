# * if / else practice
# * Rules: elif/else need an if first. else does *not* need an elif.
# * == is "same value". = is assign (would be a bug here).
# ?
# ? 5 == 6  →  False
# ? 6 == 6  →  True
# ?
# ? JS: same == for this. Python still has no ===.
# ?
# ? Last lesson (05) skipped else: return in the if, then a second return.
# ? Both work. This lesson wants the else written out.

# * Assignment: names match → high-score message, otherwise the "not" line.

def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"
