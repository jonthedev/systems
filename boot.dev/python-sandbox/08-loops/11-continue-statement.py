# * continue — skip the rest of *this* lap, go to the next i
# * The loop does not stop. Only this iteration is abandoned.
# * return would leave the whole function. continue stays in the loop.
# ?
# ? for number in range(-5, 5):
# ?     if number < 0:
# ?         continue          # skip negatives, don't print
# ?     print(number)
# ?
# ? JS: continue is the same word and the same idea.
# ?
# ? Ops flavour: for host in hosts:
# ?     if not healthy: continue
# ?     deploy(host)

# * Assignment: award every 3rd quest we actually visit (step still applies).
# * counter starts at 0. Each quest: += 1. If still < 3, continue.
# * Else: reset to 0, then print the enchantment (5 * quest_number).

def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter += 1
        if counter < 3:
            continue

        counter = 0
        enchantment_strength = quest_number * 5
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )


# Don't touch below this line


def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")


def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)


main()
