# * Order of Functions
# * A function must exist by the time it is *called*, not by the time
# * another def mentions its name.
# ?
# ? Trick: define everything first, then call one entry point (main)
# ? at the bottom. By then the interpreter has read every def.
# ?
# ? main() can call add_armor even though add_armor is written below
# ? main — because main() does not run until the last line.
# ? Same nuance as the hoisting note: the CALL time is what matters.

def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

# ? call entrypoint at the end
main()
