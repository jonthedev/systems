# * Slice with a step: list[start:stop:step]
# * Even indexes: start 0, step 2 → 0, 2, 4, ...
# * Odd indexes:  start 1, step 2 → 1, 3, 5, ...
# * Omit stop → go to the end. [0::2] is the same as [::2].
# ?
# ? players = ["Frodo", "Aragorn", "Legolas", "Gimli"]
# ? players[::2]  → ["Frodo", "Legolas"]      # even *slots*, not even names
# ? players[1::2] → ["Aragorn", "Gimli"]
# ?
# ? These are *new* lists. players itself is unchanged.
# ? return even, odd  is a tuple of two lists.
# ?
# ? JS has no step slice. You'd filter: players.filter((_, i) => i % 2 === 0)
# ?
# ? Ops flavour: split a host list into two pools — every other box.

# * Assignment: even-index players, then odd-index players.

def get_even_and_odd_teams(players):
    even_teams = players[0::2]
    odd_teams = players[1::2]
    return even_teams, odd_teams


players = [
    "Harry",
    "Hermione",
    "Ron",
    "Ginny",
    "Fred",
    "Neville",
    "Draco",
    "Luna",
    "Cho",
    "Gregory",
    "Lee",
    "Michael",
    "Lavender",
    "Frank",
    "Anthony",
    "Allan",
]

even_team, odd_team = get_even_and_odd_teams(players)
print("even:", even_team)
print("odd: ", odd_team)