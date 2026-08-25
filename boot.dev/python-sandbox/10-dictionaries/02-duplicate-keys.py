# * Keys must be unique. Write the same key twice → last value wins.
# * The first assignment is gone. No error, just a silent overwrite.
# ? JS objects are the same: { a: 1, a: 2 } keeps 2.
# ?
# ? bad = {"level": 10, "level": 99}   # level is 99, 10 never stuck
# ?
# ? This is why id was name#server — one key, one unique value.
# ? Two "level" keys would not store two levels; you'd lose one.
# ?
# ? Ops flavour: labels = {"env": "dev", "env": "prod"}
# ? You do not have both. You have prod. The first env vanished.

# * Assignment: one key each — name, server, level, rank. No duplicates.

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
    }


print(get_character_record("bloodwarrior123", "server1", 12, "gold"))