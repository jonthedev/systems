# * Changing in place
# * Update a variable using its *current* value, then store the result back.
# * Read `=` as "assign", not math-equals. Right side runs first, then it
# * overwrites the name on the left.
# ?
# ? player_score = 4
# ? player_score = player_score + 1   # now 5
# ? player_score = player_score - 1   # now 3 (if you started from 4)
# ?
# ? English: "assign to player_score: current player_score minus 1"
# ? JS: same pattern — playerScore = playerScore + 1
# ?     or the shortcut playerScore += 1  (Python has += too)

# * Assignment: add increment to current_score, return the new score.

def update_player_score(current_score, increment):
    current_score = current_score + increment
    return current_score 
