# * Set a key with the same brackets as reading: dict[key] = value
# * Missing key on *write* is fine — it creates that key. Read of a
# * missing key is still KeyError.
# ?
# ? planets = {}                    # empty dict, then fill (like [] + append)
# ? planets["Earth"] = True
# ? planets["Pluto"] = False
# ? planets["Pluto"]  → False
# ?
# ? JS: obj["Pluto"] = false   or  obj.Pluto = false
# ?
# ? Split a full name, first word = key, second = value:
# ? "jack bronson".split() → ["jack", "bronson"]
# ? names_dict["jack"] = "bronson"
# ?
# ? Ops flavour: labels = {}; labels["env"] = "prod"

full_names = ["jack bronson", "jill mcarty", "john denver"]
names_dict = {}
for full_name in full_names:
    name_parts = full_name.split()
    names_dict[name_parts[0]] = name_parts[1]

print(names_dict)
