# * if / elif / else
# * Check from the top. First True wins; the rest are skipped.
# * If none match, else runs. else is optional; at most one else.
# ?
# ? if score > high_score:
# ?     print("High score beat!")
# ? elif score > second_highest_score:
# ?     print("You got second place!")
# ? else:
# ?     print("Better luck next time")
# ?
# ? JS: else if  →  Python: elif  (one word). Same idea.
# ?
# ? Order matters: put the *narrower* check first.
# ? health <= 0 must be before health <= 5, or a dead player
# ? would match "injured" (0 is also <= 5).

# * Assignment: <= 0 dead, <= 5 injured, otherwise healthy.

def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"
