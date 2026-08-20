# * if / elif / else practice
# * Three outcomes: if → elif → else. First True wins.
# * elif = "else if" (JS). You need an if first; else does not need elif.
# ?
# ? if player_name == high_scoring_player_name:
# ?     return "high"
# ? elif player_name == low_scoring_player_name:
# ?     return "low"
# ? else:
# ?     return "neither"
# ?
# ? Check high *before* low. If the same person were both (odd but
# ? possible), they would get "high" — first match wins.

# * Assignment: match high → "high", match low → "low", else "neither".

def check_high_score(player_name, high_scoring_player_name, low_scoring_player_name):
    if player_name == high_scoring_player_name:
        return "high"
    elif player_name == low_scoring_player_name:
        return "low"
    else:
        return "neither"
