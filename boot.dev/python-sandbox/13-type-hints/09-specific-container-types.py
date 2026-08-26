# * Prefer the inside type, not just the box.
# * list          "some list"     — checker can't know items[0]
# * list[str]     list of strings — items[0] is inferred as str
# ?
# ? items: list = ["Black Firebomb", "Titanite Chunk"]      vague
# ? items: list[str] = ["Black Firebomb", "Titanite Chunk"] specific
# ?
# ? Bare list / dict / tuple isn't *illegal*. Use it when you really
# ? don't know the insides, or the full hint would be a mess.
# ? Default: be specific. That's when hover / autocomplete pay off.
# ?
# ? first_item = items[0]
# ? Before list[str]: tooltip says Unknown
# ? After  list[str]: tooltip says str  — inferred, you didn't hint
# ? first_item yourself.
# ?
# ? TS: any[] vs string[]
# ?     Record<string, unknown> vs Record<string, number>
# ? Same rule: "array" is weak. "array of strings" is the contract.
# ?
# ? Ops flavour: hosts: list vs hosts: list[str]
# ? The second one stops you treating a host like a number in the editor.

# * Assignment: list[str], dict[str, int], -> tuple[str, int]. Body unchanged.

def get_reward_summary(items: list[str], item_counts: dict[str, int]) -> tuple[str, int]:
    total_items = 0

    for count in item_counts.values():
        total_items += count

    first_item = items[0]
    return first_item, total_items


print(get_reward_summary(["potion", "sword"], {"potion": 2, "sword": 1}))
