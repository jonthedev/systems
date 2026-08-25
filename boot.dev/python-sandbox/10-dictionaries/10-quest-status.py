# * Nested dict: a value can *be* another dict. Chain keys to walk in.
# * No loop. You know the path: quests → bridge_run → status
# ?
# ? progress["quests"]["bridge_run"]["status"]
# ? JS: progress.quests.bridge_run.status
# ?     or progress["quests"]["bridge_run"]["status"]
# ?
# ? Each [...] peels one layer. Missing key at any layer → KeyError.
# ?
# ? Ops flavour: config["services"]["web"]["port"] — JSON / YAML
# ? is this shape. Nested objects, look up by name at each level.

# * Assignment: return the "bridge_run" quest status. Chain, don't loop.

def get_quest_status(progress):
    status = progress["quests"]["bridge_run"]["status"]
    return status


progress = {
    "character_name": "Kaladin",
    "quests": {
        "bridge_run": {"status": "In Progress"},
        "talk_to_syl": {"status": "Completed"},
    },
}
print(get_quest_status(progress))

