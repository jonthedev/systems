# * Same syntax as setting: dict[key] = value
# * If the key is new, it is created. If it already exists, the value
# * is *replaced* (duplicate-keys lesson: last write wins).
# ?
# ? Two jacks: first "bronson", then "denver".
# ? names_dict["jack"] ends as "denver". "bronson" is gone.
# ? james is only written once → "mcarty"
# ?
# ? JS: obj.jack = "denver"  — same overwrite.
# ?
# ? There is no "update" operator. = on an existing key *is* the update.
# ?
# ? Ops flavour: labels["env"] = "staging" after it was "dev"
# ? — one key, new value. You do not keep both envs.

full_names = ["jack bronson", "james mcarty", "jack denver"]
names_dict = {}
for full_name in full_names:
    names = full_name.split()
    first_name = names[0]
    last_name = names[1]
    names_dict[first_name] = last_name

print(names_dict)
