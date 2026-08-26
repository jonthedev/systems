# * Return hint: after the ) and before the :  use  -> Type
# * Params use `:`. Return uses `->` because there is no name for it —
# * you only care about the type that comes out.
# ?
# ? def add_gold(current_gold: int, found_gold: int) -> int:
# ? def get_greeting(player_name: str) -> str:
# ?
# ? With in-types and out-type, you can *call* the function without
# ? reading the body. That's the point of a signature.
# ?
# ? TS: function getItemDescription(...): string
# ? Python `-> str`  ≈  TS `: string` after the param list.
# ?
# ? Still a note, not a gate. Returning the wrong type still *runs*.
# ? A checker will squiggle a `return 42` on a `-> str` function.
# ?
# ? Ops flavour: def is_healthy(host: str) -> bool
# ? Callers know they get True/False, not a status string.

# * Assignment: add -> str. Don't change the body.

def get_item_description(item_name: str, damage: int, is_magical: bool) -> str:
    description = f"{item_name} deals {damage} damage"

    if is_magical:
        description += " and glows with arcane power"
    else:
        description += " and has no magical properties"

    return description


print(get_item_description("staff", 12, True))
