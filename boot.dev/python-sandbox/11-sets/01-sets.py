# * set — a bag of unique values. No duplicates. Unordered (unlike lists,
# * and unlike dicts on 3.7+). Loop order is not a promise.
# * Curly braces like a dict, but *no* key: value — just values.
# ?
# ? {"apple", "banana", "apple"} → {"apple", "banana"}  (one apple)
# ? {} is an empty *dict*. Empty set is set().
# ?
# ? .add() is append for sets. Adding a value already there is a no-op.
# ?
# ? Deduplicate a list: list → set → list
# ? Order of the result may shuffle. You asked for unique, not "same order."
# ? The longer walk (seen-set + append) keeps first-seen order if you need it.
# ?
# ? JS: [...new Set(spells)]  — same unique-then-array idea.
# ?
# ? Ops flavour: unique hostnames from a noisy scrape. One web-1 is enough.

# * Assignment: return a list with each spell at most once.

def remove_duplicates(spells):
    spell_set = set(spells)
    spell_list = list(spell_set)
    return spell_list


# * Iteration: seen-set remembers names, unique list keeps first-seen order.
# * if spell not in seen  — same `in` as dict keys. Set membership, not a loop.
# * First time: add to the set *and* append to the list.
# * Second time: skip. The list never gets a duplicate.

def remove_duplicates_keep_order(spells):
    seen = set()
    unique = []
    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            unique.append(spell)
    return unique


spells = ["fireball", "heal", "fireball", "frost", "heal"]
print("conversion: ", remove_duplicates(spells))
print("keep order:", remove_duplicates_keep_order(spells))

