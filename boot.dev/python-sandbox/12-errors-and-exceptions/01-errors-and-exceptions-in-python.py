# * SyntaxError: the file isn't valid Python. Never even runs. Can't catch it
# * in the same file — the interpreter already refused the source.
# * Exception: syntax is fine, something blew up *while running*
# * (10/0, missing key, "player id not found").
# ?
# ? try:     run this
# ? except:  only if something in try raised
# ?
# ? except Exception as e:  e is the error object. print(e) is the message.
# ? JS: try { ... } catch (e) { console.log(e.message) }
# ? Python `raise` = JS `throw`. `except` = `catch`.
# ?
# ? One try around five calls: first raise *stops* the try. Later prints
# ? never run. Id 4 raises, so 5 (Gandalf) is skipped. That's the assignment.
# ?
# ? Wrapping keeps the process alive — handle it, don't crash.
# ? Ops flavour: missing host in a lookup. Log the error, keep going
# ? (or stop this batch). Don't take down the whole script.

# * Assignment: wrap the five get_player_record calls; print the exception.

def main():
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
        print(get_player_record(5))
    except Exception as e:
        print(e)


# Don't edit below this line


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    if player_id == 5:
        return {"name": "Gandalf", "level": 5000}
    raise Exception("player id not found")


main()