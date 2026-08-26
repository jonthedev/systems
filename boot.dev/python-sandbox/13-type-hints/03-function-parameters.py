# * Param hint: def f(name: Type):  — same colon syntax as a variable.
# * Each param can have its own type. Body stays the same.
# ?
# ? def greet_player(name: str):
# ? def add_gold(current_gold: int, found_gold: int):
# ?
# ? Variable hint is often redundant (72.5 already screams float).
# ? Param hints are *not* redundant: nothing is assigned yet, so the
# ? editor can't infer. No hint → params show as "unknown".
# ?
# ? Hover `status` after you hint the params: tooltip can say it's a str
# ? because it was built from hinted pieces.
# ?
# ? TS: function getCharacterStatus(name: string, level: number, ...)
# ? Same idea. Python still won't crash on a wrong call at run time.
# ?
# ? Ops flavour: def ping(host: str, timeout: int) — the signature is
# ? the docs. You don't have to open the body to know what to pass.

# * Assignment: hint name, level, health, has_magic. Don't change the body.

def get_character_status(name: str, level: int, health: float, has_magic: bool):
    status = f"{name} is level {level} with {health} HP"

    if has_magic:
        status += ", and can cast spells"
    else:
        status += ", and cannot cast spells"

    return status


print(get_character_status("Gandalf", 80, 99.5, True))
