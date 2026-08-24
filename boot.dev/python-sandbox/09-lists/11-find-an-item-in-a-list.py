# * No-index in the wild: for item in items — you want the name, not the slot.
# * Flag pattern: start found = False, flip to True if you ever see a match.
# * After the loop, return that flag (True or still False).
# ?
# ? if item == "Leather Scraps":   # parens around the test are optional
# ?     found = True
# ?     break                      # optional: stop once you know it's there
# ?
# ? JS: for (const item of items) { if (item === "Leather Scraps") found = true }
# ? Later: "Leather Scraps" in items  — same answer, no loop. Not this lesson.
# ?
# ? Ops flavour: is "web-1" in the host list? Walk names until you see it.

# * Assignment: if any item is Leather Scraps, set found = True.

def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if(item == 'Leather Scraps'):
            found = True
            break

    # don't touch below this line

    return found


has_scraps = ["Healing Potion", "Leather Scraps", "Iron Helmet"]
no_scraps = ["Healing Potion", "Iron Helmet", "Bread"]
print("with scraps:   ", contains_leather_scraps(has_scraps))
print("without scraps:", contains_leather_scraps(no_scraps))