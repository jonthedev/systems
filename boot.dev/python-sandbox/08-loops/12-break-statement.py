# * break — leave the loop entirely. Remaining iterations never run.
# * continue skips this lap. break walks out. The loop is done.
# * return would leave the whole function. break only leaves the loop
# * (code after the loop still runs).
# ?
# ? for n in range(42):          # would go 0..41, but...
# ?     print(n * n)
# ?     if n * n > 150:
# ?         break                # 13*13=169, then stop. Never reach 41.
# ?
# ? JS: break is the same word and the same idea.
# ?
# ? Ops flavour: for host in hosts:
# ?     if deploy(host):
# ?         break                # first success is enough; stop trying

# * Assignment: compare each enchantment to the attack.
# * If one is >= attack_strength, print "Attack blocked!" then break.
# * Don't keep comparing after you've already blocked it.

def check_defense(attack_strength, min_enchantment, max_enchantment):
    for enchantment_strength in range(min_enchantment, max_enchantment + 1):
        print(
            f"Comparing attack strength {attack_strength} to enchantment strength {enchantment_strength}."
        )

        if enchantment_strength >= attack_strength:
            print("Attack blocked!")
            break


# Don't touch below this line


def test(attack_strength, min_enchantment, max_enchantment):
    print(
        f"Testing attack strength {attack_strength} vs. enchantment strengths {min_enchantment}–{max_enchantment}:"
    )
    check_defense(attack_strength, min_enchantment, max_enchantment)
    print("========================================")


def main():
    test(5, 8, 12)
    test(8, 6, 10)
    test(10, 5, 8)
    test(7, 4, 7)


main()