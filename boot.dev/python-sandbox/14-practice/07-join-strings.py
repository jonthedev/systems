# * Glue with commas: add "name," every time, then chop the extra comma.
# * joined[:-1]  — slice off the last character. Don't use ",".join(...) here.
# ?
# ? ["Annie", "Reiner", "Bertholdt"]
# ?   "Annie," + "Reiner," + "Bertholdt,"  →  "Annie,Reiner,Bertholdt,"
# ?   [:-1] strips the trailing comma        →  "Annie,Reiner,Bertholdt"
# ?
# ? []  →  joined stays "".  ""[:-1] is still "". No special empty-case if.
# ? One item: "Annie,"[:-1] → "Annie"
# ?
# ? += s + ","  is the same in-place add you've used on numbers, but for strings.
# ? (Python builds a new string each +=. Fine at this size. .join is faster later.)
# ?
# ? JS: names.join(",") — Python's is reversed: ",".join(names)
# ? You already used join in filter_messages. This lesson rebuilds it by hand.
# ?
# ? Ops flavour: hosta,hostb,hostc for an allowlist. Trailing comma
# ? often breaks parsers — that's the [:-1].

# * Assignment: join with commas between. Empty list → "". No .join().

def join_strings(strings: list[str]) -> str:
    joined = ""
    for s in strings:
        joined += s + ","
    return joined[:-1]


print(join_strings(["Annie", "Reiner", "Bertholdt"]))
print(join_strings(["Eren", "Mikasa", "Armin"]))
print(join_strings([]))
