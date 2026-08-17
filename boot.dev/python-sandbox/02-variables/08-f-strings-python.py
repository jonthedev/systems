# * F-strings
# * Strings that contain dynamic values. Add f before the quotes.

# ? num_bananas = 10
# ? bananas = f"You have {num_bananas} bananas"
# ? print(bananas)
# ? # You have 10 bananas
# ? Curly braces {variable} insert the value. You can pass an f-string
# ? straight into print() — it is still just a string.

# ? JS template literal: `You have ${num_bananas} bananas`
# ? Python f-string:     f"You have {num_bananas} bananas"
# ? Python uses { } not ${ }. The f at the front is required.

# * Assignment
# ? Inject name, race, and age. Do not hard-code "Yarl" / "dwarf" / 37.

name = "Yarl"
age = 37
race = "dwarf"

# ? Don't edit above this line
print(f"{name} is a {race} who is {age} years old.")
