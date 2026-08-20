# * if practice — early return
# * Last lesson: no return, so the next line always ran.
# * Here: return inside the if *exits*. The other return is the "else"
# * without writing else yet.
# ?
# ? is_equal = 5 == 5   # True
# ?
# ? if number_of_swords == number_of_soldiers:
# ?     return "correct amount"
# ? return "incorrect amount"
# ?
# ? Python: parens around the condition are optional (JS requires them).
# ? Strings must match exactly — no extra punctuation.

# * Assignment: equal counts → "correct amount", otherwise "incorrect amount".

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if(number_of_swords == number_of_soldiers):
        return "correct amount"
    return "incorrect amount"
