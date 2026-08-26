# * Nested hint: a container *inside* a container.
# * Read from the outside in.
# ?
# ? character_spells: dict[str, list[str]] = {
# ?     "Gandalf": ["Fireball", "Light"],
# ?     "Frodo": ["Hide"],
# ? }
# ?
# ? dict[str, list[str]]
# ?   dict          — the outer box is a dictionary
# ?   str           — each key is a string (the name)
# ?   list[str]     — each value is a list of strings (the spells)
# ?
# ? Same trick as before: first = keys, second = values.
# ? The "value" slot just happens to be another container.
# ?
# ? Quiz: tuple[str, list[int]]
# ? A pair: [0] is a str, [1] is a list of ints.
# ? Not "a list of tuples". Outer type is still the tuple.
# ?
# ? Deep nesting can look ugly. Still clearer than no types.
# ? If it gets too nested, that's a smell — maybe a named structure later.
# ?
# ? TS: Record<string, string[]>
# ?     [string, number[]]
# ? Brackets nest the same way: outside-in.
# ?
# ? Ops flavour: dict[str, list[str]]
# ? hostname → list of open ports as strings, or service → list of hosts.

# * This lesson is a quiz, not a function to fix. Run the example.

character_spells: dict[str, list[str]] = {
    "Gandalf": ["Fireball", "Light"],
    "Frodo": ["Hide"],
}

print(character_spells)
print(character_spells["Gandalf"][0])
