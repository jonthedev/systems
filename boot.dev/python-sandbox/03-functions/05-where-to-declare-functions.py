# * Where to declare functions
# * Code runs top to bottom. A name must exist before you use it.

# ? print(my_name)
# ? my_name = "Lane Wagner"
# ? # NameError: 'my_name' is not defined
# ?
# ? my_name = "Lane Wagner"
# ? print(my_name)  # works

# ? Functions are the same: def first, then call.
# ? JS function declarations are hoisted (you can call before the line).
# ? Python does not hoist. def main(): must sit above main().

# * Assignment
# ? Call was above the def. Move the call below (NameError otherwise).

def main():
    print("Fantasy Quest is booting up...")
    print("Game is running!")

main()
