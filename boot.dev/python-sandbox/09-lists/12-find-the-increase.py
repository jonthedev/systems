# * Two lists, same length, same slots: i is the character's position in both.
# * This is why we still need the index — no-index would give one value, not a pair.
# ?
# ? old[i] < new[i]  → they leveled up → print i (the slot, not the level)
# ? old[i] == new[i] → no change, print nothing
# ? old[i] > new[i]  → somehow down, print nothing
# ?
# ? Example: old = [2, 5, 3, 7, 5]
# ?          new = [2, 5, 19, 7, 8]
# ?          prints 2 and 4  (3→19 and 5→8)
# ?
# ? JS: for (let i = 0; i < old.length; i++) {
# ?       if (old[i] < new[i]) console.log(i)
# ?     }
# ?
# ? Ops flavour: yesterday_cpu[i] vs today_cpu[i] on the same host list.

# * Assignment: print each index where the new level is higher.

def check_character_levels():
    old_character_levels = [1, 42, 43, 53, 12, 3, 32, 34, 54, 32, 43]
    new_character_levels = [1, 42, 45, 54, 12, 3, 32, 38, 54, 32, 42]

    # don't touch above this line

    for i in range(0, len(old_character_levels)):
        old_c_level = old_character_levels[i]
        new_c_level = new_character_levels[i]

        if(old_c_level < new_c_level):
            print(i)


# don't touch below this line


def test():
    print("Character level increased at indexes:")
    check_character_levels()
    print("=====================================")


def main():
    test()


main()




