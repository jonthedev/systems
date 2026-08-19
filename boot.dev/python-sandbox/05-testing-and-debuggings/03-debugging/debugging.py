# * Debugging
# * Write code → run it → if it is wrong, fix it. Repeat until you trust it.
# * Boot.dev Run = debug (some tests). Submit = "ship it" (all tests).
# * You are not punished for hitting Run. Submit with a fail is the
# * production-shaped slap.
# ?
# ? Debug with print(): compute a value, print it, Run, does it match
# ? what you expected? Fix, repeat. Unit-test lessons ignore prints.

# * Assignment
# ? New health after magic damage:
# ?   max damage  = spell_power * amp
# ?   actual      = max damage - resist
# ?   new health  = health - actual
# ? Example: health 100, resist 5, amp 2, spell 20
# ?   20*2=40, 40-5=35, 100-35=65

def take_magic_damage(health, resist, amp, spell_power):
    total_maximum_damage = spell_power * amp
    total_damage = total_maximum_damage - resist
    return health - total_damage
