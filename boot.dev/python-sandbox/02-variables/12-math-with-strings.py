# * Math With Strings
# * On strings, + means concatenate (join), not add numbers.

# ? first_name = "Lane "
# ? last_name = "Wagner"
# ? full_name = first_name + last_name
# ? print(full_name)  # Lane Wagner
# ? The space lives in "Lane " — + does not insert spaces for you.

# ? Prefer f-strings over + for real work:
# ? f"{first_name}{last_name}"
# ? JS: "You have " + health  vs  `You have ${health}`
# ? Same trap: "1200" is text. 1200 is a number. "12" + "00" is "1200",
# ? not 12.

# * Assignment
# ? Print each player's health with concatenation and the given variables.

sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# ? Don't edit above this line
print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)

# ? Same result, what you'd write for real:
# ? print(f"You have {player1_health} health")
# ? print(f"You have {player2_health} health")
