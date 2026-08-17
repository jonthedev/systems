# * Multiple Parameters
# * A function can take more than one input. Names in the def are
# * parameters. Values you pass in are arguments, in order.

# ? def subtract(a, b):
# ?     result = a - b
# ?     return result
# ? result = subtract(5, 3)  # a=5, b=3 → 2
# ? First argument → first parameter, second → second. Same as JS.

# ? Four inputs still just a comma list:
# ? create_introduction(my_name, my_age, "1.8", "80")

# * Assignment
# ? Return the sum of damage_one, damage_two, damage_three.

def triple_attack(damage_one, damage_two, damage_three):
    total = damage_one + damage_two + damage_three
    return total

# ? Don't touch below this line
# This is the first triple attack
attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

# This is the second triple attack
attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")
