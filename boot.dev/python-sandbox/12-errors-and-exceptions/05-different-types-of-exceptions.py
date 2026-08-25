# * Different exception *types*. Python matches except top to bottom and
# * stops at the first match. Put the *specific* one first.
# ?
# ? IndexError     — list slot does not exist (players[3] on a 3-item list)
# ? ZeroDivisionError — 10/0
# ? Exception      — the general bag. Catches almost everything.
# ?
# ? except IndexError:          # specific first
# ? except Exception as e:      # leftover errors, `e` is the object
# ?
# ? If Exception is first, IndexError never gets its own handler.
# ?
# ? JS: one catch, then if (e instanceof RangeError). Python: several excepts.
# ?
# ? get_player_record: id < 0 → Exception("negative ids not allowed")
# ?                   id 3+   → IndexError from players[id]
# ?                   0,1,2   → the dict, no error
# ?
# ? Ops flavour: FileNotFoundError vs a generic Exception — different
# ? messages, different next step (create the file vs abort).

# * Assignment: IndexError → "index is too high". Anything else → return e.

def process_player_record(player_id):
    try:
        return get_player_record(player_id)
    except IndexError:
        return "index is too high"
    except Exception as e:
        return e
        

# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]


print("ok:      ", process_player_record(0))
print("too high:", process_player_record(9))
print("negative:", process_player_record(-1))