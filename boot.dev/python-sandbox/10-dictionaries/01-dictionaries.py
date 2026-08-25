# * dict — key → value pairs. JS calls this an object.
# * Curly braces. Keys are usually strings. Look up by name, not by index 0, 1, 2.
# ?
# ? car = {
# ?     "brand": "Toyota",
# ?     "model": "Camry",
# ?     "year": 2019,
# ? }
# ? car["brand"] → "Toyota"
# ?
# ? JS: { brand: "Toyota", model: "Camry" }  — quotes on keys are optional there.
# ? Python keys in a literal are quoted if they are strings.
# ?
# ? id = f"{name}#{server}"  → "bloodwarrior123#server1"
# ? (same idea as Discord user#tag, or host.region)
# ?
# ? Ops flavour: a box is not a list of facts. It is a record:
# ? {"name": "web-1", "role": "web", "cpu": 2}

# * Assignment: return a character dict; id is name#server.

def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}",
    }


print(get_character_record("bloodwarrior123", "server1", 12, "gold"))