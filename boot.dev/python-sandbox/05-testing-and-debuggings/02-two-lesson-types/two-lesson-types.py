# * Two lesson types on Boot.dev
# *
# * 1. Console output — pass if print() matches exactly.
# *    Debug prints will fail you. Chapters 1–4 were this.
# *
# * 2. Unit-test — two files: your code (main.py) + tests
# *    (main_test.py). Tests call your functions and check
# *    *return* values. Prints are ignored, so you can leave
# *    debug print() in. Like Vitest: expect(fn(x)).toBe(y)
# *    not "did the console log the right string."
# *
# * Going forward: mostly unit-test lessons, sometimes still
# * console output. Tests stay on Boot.dev — we do not copy
# * main_test.py. pytest later, when we write tests ourselves.
