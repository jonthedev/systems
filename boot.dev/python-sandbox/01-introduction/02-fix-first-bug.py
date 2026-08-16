# * The combat system in Fantasy Quest isn't working as intended!
# * Players were gaining health when attacked instead of losing it.

# ? Subtract damage from health (do not add).
sword_damage = 10
start_health = 100
end_health = start_health - sword_damage

# ? Don't touch below this line
print(f"Sam's health is: {start_health}")
print(f"Sam takes {sword_damage} damage...")
print(f"Sam's health is: {end_health}")
