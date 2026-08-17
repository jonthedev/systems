# * Dynamic Typing
# * A name can hold any type, and that type can change later.

# ? speed = 5
# ? speed = "five"  # allowed in Python. The name now points at a str.

# * But like, maybe don't
# ? Changing a variable's type is almost always a bad idea.
# ? Make a new name instead:
# ? speed = 5
# ? speed_description = "five"

# * Static typing
# ? Go and TypeScript check types before the program runs.
# ? If Python were static, speed = "five" after speed = 5 would
# ? fail: you cannot put a string in a number variable.
# ? JS without TypeScript is dynamic too — this is not Python-only.
# ? Type hints (later) are labels; they do not enforce this at runtime.
