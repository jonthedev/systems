# * Debugging practice
# * Their walkthrough: tiny steps, print, Run, then the next line.
# * That is for when you do *not* already see the answer.
# * You already ship JS — sum + an f-string in one go is fine.
# * Use print() when a test fails and you cannot see why, not as ritual.

# * Assignment
# ? Return two values (a tuple, same as functions chapter):
# ?   1. before_xp + ach_xp
# ?   2. "Achievement Unlocked: {name}"
# ? Their demo had fake bugs (minus instead of plus, missing Unlocked)
# ? so you would catch them with print. You skipped that — fair.

def unlock_achievement(before_xp, ach_xp, ach_name):
    player_xp = before_xp + ach_xp
    message = f"Achievement Unlocked: {ach_name}"
    return player_xp, message
