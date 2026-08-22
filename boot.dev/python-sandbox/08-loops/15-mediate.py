# * while + and: keep going only while BOTH stay true.
# * Stop at the first brake: mana is full, *or* potions run out.
# * Each lap: drink one potion → mana += 1, num_potions -= 1.
# ?
# ? mana=3, max=5, potions=10 → drink 2, stop at full, 8 left
# ? mana=3, max=10, potions=2 → drink 2, stop at empty, mana=5
# ? mana=5, max=5, potions=3  → while never runs (already full)
# ?
# ? return mana, num_potions — two values. Python just lists them.
# ? JS would pack them: return [mana, numPotions]
# ?
# ? JS: while (mana < maxMana && numPotions > 0) { mana++; numPotions--; }
# ?
# ? Ops flavour: scale up while under capacity AND budget left.
# ? Same two-brake pattern as regenerate (health + enemy distance).

# * Assignment: consume potions one at a time until full or empty.

def meditate(mana, max_mana, num_potions):
    while mana < max_mana and num_potions > 0:
        mana += 1
        num_potions -= 1
    return mana, num_potions