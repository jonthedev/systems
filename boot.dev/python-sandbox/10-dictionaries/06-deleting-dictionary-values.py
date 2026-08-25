# * del dict[key] — drop that key (and its value). Mutates in place.
# * Same keyword as list deletion, but you name the *key*, not an index.
# ? Missing key → KeyError (same crash as reading a missing key).
# ?
# ? names_dict = {"jack": "bronson", "jill": "mcarty", "joe": "denver"}
# ? del names_dict["joe"]
# ? # {"jack": "bronson", "jill": "mcarty"}
# ?
# ? del names_dict["unknown"]  → KeyError
# ?
# ? JS: delete obj.joe  — missing key is usually a no-op, not a crash.
# ? Python is louder again.
# ?
# ? Ops flavour: del labels["env"]  — that field is gone, not set to None.

names_dict = {"jack": "bronson", "jill": "mcarty", "joe": "denver"}
del names_dict["joe"]
print(names_dict)
