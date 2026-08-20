# * Comparison operators → always True or False (boolean)
# * Same symbols as JS:
# ? <   less than
# ? >   greater than
# ? <=  less than or equal
# ? >=  greater than or equal
# ? ==  equal
# ? !=  not equal
# ?
# ? 5 < 6   →  True
# ? 5 > 6   →  False
# ? 5 >= 6  →  False
# ? 5 <= 6  →  True
# ? 5 == 6  →  False
# ? 5 != 6  →  True
# ?
# ? JS trap: Python has no ===. == is the equality check.
# ?          (Later: `is` is "same object", not "same value".)
# ?
# ? Ops flavour: if replica_count < 3: scale up
# ?              if exit_code != 0: fail the job

# * Assignment: True if player 1's score is *strictly* higher (ties → False).

def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score
