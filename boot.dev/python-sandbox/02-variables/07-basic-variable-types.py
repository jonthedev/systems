# * Basic Variable Types
# * Python has several basic data types. The type lives on the value,
# * not on a let/const keyword.

# * Strings
# * Snippets of text: characters strung together. Wrap them in quotes.
# * Single or double both work; double quotes are the usual style.

# ? name_with_single_quotes = 'boot.dev'  # works, less common
# ? name_with_double_quotes = "boot.dev"  # preferred
# ? JS: same idea as "boot.dev" / 'boot.dev'

# * Numbers
# * No quotes. Quotes would make a string ("5" vs 5).

# ? Integer (int): no decimal — x = 5, y = -5
# ? Float: has a decimal — x = 5.2, y = -5.2
# ? JS number is one type for both; Python splits int and float.

# * Booleans
# * A bool is only True or False. Computers' 1s and 0s are this idea.

# ? is_tall = True
# ? is_short = False
# ? JS uses lowercase true / false. Python capitalizes True / False.

# * Assignment
# ? player_health should be an int. player_has_magic should be a bool.

player_health = 100
player_has_magic = True

# ? don't touch below this line
print("player_health is a/an", type(player_health).__name__)
print("player_has_magic is a/an", type(player_has_magic).__name__)
