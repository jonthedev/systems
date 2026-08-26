# * A type hint only helps if it matches what the code actually does.
# * Return a string → hint should be -> str. Wrong hint = a lying contract.
# ?
# ? Python still *runs* a mismatch. The checker (Pylance / Boot.dev editor)
# ? is what draws the red squiggle: "you promised str, you returned int".
# ?
# ? Wrong:  def get_greeting(player_name: str) -> int:
# ? Right:  def get_greeting(player_name: str) -> str:
# ? The f-string is already a str. Only the hint was wrong — not the body.
# ?
# ? TS: if you annotate `: number` but return a string, tsc complains.
# ? Python: no tsc. You (or Pylance) have to notice the lie.
# ?
# ? Ops flavour: def get_status(host: str) -> str
# ? Callers trust the signature. If it really returns a dict, they break
# ? later — the hint hid the truth.

# * Assignment: fix the return hint to str. Don't change the body.

def get_greeting(player_name: str) -> str:
    return f"Welcome to Fantasy Quest, {player_name}!"


print(get_greeting("Boot"))
