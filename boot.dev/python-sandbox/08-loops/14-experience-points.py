# * Accumulator: start at 0, add a chunk each lap, return the running total.
# * Level 1 has paid nothing yet → 0. To *be* at `level`, you already paid
# * the cost of every earlier level: 1*5 + 2*5 + ... + (level-1)*5.
# ?
# ? level 1: range(1, 1) is empty → 0
# ? level 2: 1*5                    → 5
# ? level 3: 1*5 + 2*5              → 15
# ? level 4: 1*5 + 2*5 + 3*5        → 30
# ?
# ? range(1, level) stops *before* level. Do not add level*5 — that is
# ? the cost to *leave* this level, not XP already gained.
# ?
# ? JS: let total = 0; for (let i = 1; i < level; i++) total += i * 5;
# ?
# ? Ops flavour: cost to reach N replicas = sum of scale-up steps so far,
# ? not the price of the next one you have not bought yet.

# * Assignment: given current level, return XP gained so far.

def calculate_experience_points(level):
    total_xp = 0
    for i in range(1, level):
        new_xp = i * 5
        total_xp += new_xp
    return total_xp

print(calculate_experience_points(1))




