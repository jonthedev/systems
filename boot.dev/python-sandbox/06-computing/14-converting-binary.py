# * Convert a binary *string* to an int:  int(s, 2)
# * Lesson 10: 0b100 is a number you typed as binary.
# * This lesson: "100" is text. Python does not assume it's binary
# * unless you pass base 2.
# ?
# ? int("100")      →  100    default base 10 (looks like one hundred)
# ? int("100", 2)   →  4      read as binary (4+0+0)
# ? int("101", 2)   →  5
# ? int("10010", 2) →  18
# ?
# ? JS: parseInt("100", 2)  →  4     same second-arg "base"
# ?     parseInt("100")     →  100
# ? 0b prefix is for *literals* in source. Strings need int(..., 2).

# * Assignment: three binary strings in, three ints out (same order).

def binary_string_to_int(num_servers, num_players, num_admins):
    num_servers = int(num_servers, 2)
    num_players = int(num_players, 2)
    num_admins = int(num_admins, 2)
    return num_servers, num_players, num_admins
