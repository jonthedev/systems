# * Site-only lesson. No function to retype here.
# * Boot.dev: add one more dict to their test_cases list. That's the whole task.
# * We don't copy test_cases.py / main_test.py — the site is the grader
# * (same rule as 05-testing-and-debuggings/README.md).
# ?
# ? A test case is usually a dict of "what I pass" + "what I should get":
# ?   {"input": ..., "expected": ...}
# ? Adding one = one more contract, not new production code.
# ?
# ? TS/Vitest: it("...", () => expect(fn(input)).toBe(expected))
# ? Same idea: input/output pair. They stored those pairs as dicts in a list.
# ?
# ? Ops flavour: a table of examples (host → expected status). Extra row,
# ? not a new script.

# * Skip local run. Next: 09-fix-a-failing-test.py (also site-only).
