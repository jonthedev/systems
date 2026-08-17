# * Multiple Return Values
# * return a, b sends two values out. Order matters, names inside
# * the function do not leak out (that is scope — next chapter).

# ? def cast_iceblast(wizard_level, start_mana):
# ?     damage = wizard_level * 2
# ?     new_mana = start_mana - 10
# ?     return damage, new_mana
# ?
# ? damage, mana = cast_iceblast(5, 100)
# ? First returned value → first name, second → second.
# ? JS usually returns one thing (array or object) and unpacks it.
# ? Python: commas on both sides.

# * Assignment
# ? title: f"{full_name} the warrior"  (spaces exact)
# ? new_power: power + 1
# ? return both

def become_warrior(full_name, power):
    title = f"{full_name} the warrior"
    new_power = power + 1
    return title, new_power


# ? Don't edit below this line
def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()
