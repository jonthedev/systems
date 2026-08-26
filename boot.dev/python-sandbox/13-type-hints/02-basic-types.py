# * Variable hint: name: Type = value  — colon, type, then =.
# * The value is unchanged. The hint is a label, not a conversion.
# ?
# ? str    string     "Gandalf"     TS: string
# ? int    whole num  80            TS: number (TS doesn't split int/float)
# ? float  decimal    99.5          TS: number
# ? bool   True/False True          TS: boolean  (capital T/F in Python)
# ?
# ? Often you can skip the hint:  health = 72.5
# ? The editor infers float from the value. Hint is optional on a simple =
# ? Useful when you want the type *visible*, or the value isn't obvious.
# ?
# ? Mismatch:  level: str = 80  — still *runs*. Checker squiggles it.
# ? That's the red lines Boot.dev mentioned. Python itself doesn't care.
# ?
# ? Ops flavour: timeout: int = 30  — seconds, not "30" as a string.

# * Assignment: fix the hints, not the values.

character_name: str = "Gandalf"
character_level: int = 80
character_health: float = 99.5
has_magic: bool = True

print(character_name, character_level, character_health, has_magic)
