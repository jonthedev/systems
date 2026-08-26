# * When the hint and the body disagree, one of them is lying.
# * If the *signature* is the contract, treat it as the source of truth
# * and fix the implementation — not the hint.
# ?
# ? -> list[tuple[str, int]]
# ?   a list of pairs: (quest name: str, xp: int)
# ?
# ? The bug:  summary.append(quest_xp)
# ?   quest_xp is an int. That builds list[int], which fights the hint.
# ? The fix:  summary.append((quest_name, quest_xp))
# ?   a tuple. Extra ( ) so append gets one pair, not two arguments.
# ?
# ? Nested read, outside-in:
# ?   list[tuple[str, int]]  →  list of  (str, int)  pairs
# ?
# ? TS: [string, number][]   or  Array<[string, number]>
# ? Pushing a bare number into that array is the same class of bug.
# ?
# ? Ops flavour: -> list[tuple[str, int]]
# ? hostname + port, or service + replica count. The pair *is* the row.
# ? Appending only the int would silently drop the name.

# * Assignment: fix the body. Don't change the signature.

def summarize_quest_rewards(
    completed_quests: list[str], quest_rewards: dict[str, int]
) -> list[tuple[str, int]]:
    summary: list[tuple[str, int]] = []

    for quest_name in completed_quests:
        if quest_name in quest_rewards:
            quest_xp = quest_rewards[quest_name]
            summary.append((quest_name, quest_xp))

    return summary


print(
    summarize_quest_rewards(
        ["slay dragon", "fetch water", "unknown"],
        {"slay dragon": 500, "fetch water": 10},
    )
)
