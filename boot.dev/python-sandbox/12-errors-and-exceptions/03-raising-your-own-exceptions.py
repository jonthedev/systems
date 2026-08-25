# * raise when *your* function hits a bad input — unknown id, invalid metal.
# * That is not a bug if the caller is supposed to handle it. A bug is
# * silently forging a gold sword that does not exist in the game.
# ?
# ? Do NOT try/except your own raise in the same function. Let the caller
# ? decide: log it, show the player, or crash. Tests wrap the call.
# ?
# ? # don't: raise inside, then except in the same def
# ? # do:    raise here;  try: get_player_record(4)  except: ...  at the call site
# ?
# ? JS: throw in the helper, catch in the caller. Same split.
# ?
# ? Ops flavour: lookup_host("nope") raises. The script that called it
# ? logs and skips. The lookup function does not print and pretend.

# * Assignment: unknown player_id → raise Exception("player id not found")
# * Do not catch it here.

def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")


print(get_player_record(1))
try:
    get_player_record(4)
except Exception as e:
    print(e)
