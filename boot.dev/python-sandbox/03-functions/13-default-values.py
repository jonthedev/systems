# * Default Values
# * A parameter can have a fallback if the caller omits it.
# * Write it with = in the def. Optionals must come AFTER required ones.

# ? def get_greeting(email, name="there"):
# ?     print("Hello", name + ", welcome! You've registered:", email)
# ? get_greeting("lane@example.com", "Lane")  # uses "Lane"
# ? get_greeting("lane@example.com")          # uses "there"
# ? JS: function getGreeting(email, name = "there") { ... }

# * Assignment
# ? armor defaults to 0 (no armor).
# ? punch damage = 50 - armor. slash damage = 100 - armor.
# ? Return health after that damage.

def get_punched(health, armor=0):
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor=0):
    damage = 100 - armor
    new_health = health - damage
    return new_health


# ? Don't touch below this line
def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)
