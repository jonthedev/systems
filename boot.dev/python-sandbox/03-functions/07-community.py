# * Community
# * Boot.dev Discord is their help channel (spellbook / Boots first,
# * humans when stuck). Not needed in this repo.

# * Assignment
# ? Convert Fahrenheit f to Celsius: 5/9 * (f - 32)
# ? Return it. Do not print inside to_celsius.

def to_celsius(f):
    return 5 / 9 * (f - 32)


# ? Don't touch below this line
# ? test() is just a helper that prints — not pytest.


def test(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test(100)
test(88)
test(104)
test(112)
