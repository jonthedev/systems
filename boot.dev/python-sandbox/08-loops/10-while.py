# * while — keep going *as long as* the condition is True
# * `for` when you know how many times (range). `while` when you stop
# * because something in the world changed.
# ?
# ? num = 0
# ? while num < 3:
# ?     num += 1
# ?     print(num)      # 1 2 3  then num is 3, condition fails, stop
# ?
# ? You *must* change something the condition cares about, or it never ends.
# ? while True:  (or while 1:) is an infinite loop — Ctrl+C to kill.
# ?
# ? JS: while (num < 3) { num += 1 }  same idea. Indent + : in Python.

# * Assignment: regen 1 HP per tick while not full AND enemy farther than 3.
# * Each tick: health += 1, enemy_distance -= 2. Then return health.
# ? and: both must stay True. Distance 3 is *not* > 3, so regen stops.

def regenerate(current_health, max_health, enemy_distance):
    while current_health < max_health and enemy_distance > 3:
        current_health += 1
        enemy_distance -= 2

    return current_health
