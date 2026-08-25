# * Read a value with square brackets and the *key*, not an index.
# * dict["make"]  — same brackets as list[0], but the slot is a name.
# ?
# ? car = {"make": "Toyota", "model": "Camry"}
# ? car["make"]  → "Toyota"
# ? car["year"]  → KeyError   # missing key crashes. JS would give undefined.
# ?
# ? JS: car.make  or  car["make"]
# ? Python has no car.make for dicts (that's an attribute, different thing).
# ?
# ? Ops flavour: host["role"]  — the value for that field, not hosts[0].

car = {"make": "Toyota", "model": "Camry"}
print(car["make"])
