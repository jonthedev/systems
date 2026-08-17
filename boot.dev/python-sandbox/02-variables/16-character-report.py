# * Character Report
# * Chapter wrap: types have to match what the report expects.
# ? name: str
# ? level: int
# ? character_class: str
# ? magic_resistance: float  (10.5 not "10.5" or 10)
# ? account_active: bool     (True / False, not "True")

name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 10.5
account_active = True

# ? Don't edit below this line
print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")
