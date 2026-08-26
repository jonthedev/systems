# * Site-only lesson. Same as 08 — no function to retype here.
# * Boot.dev: a test was failing. The job was to fix the *case*
# * (the dict in test_cases), not to copy their harness locally.
# * We don't copy test_cases.py / main_test.py — the site is the grader
# * (same rule as 05-testing-and-debuggings/README.md).
# ?
# ? When a test fails, two things might be lying:
# ?   the function (implementation)  or  the expected value (the test).
# ? This lesson: the test case was wrong. Edit the dict, re-run.
# ?
# ? TS/Vitest: expected 4, got 5 → either the code or the expect() is wrong.
# ? Don't "make the test pass" by weakening it unless the expect was the bug.
# ?
# ? Ops flavour: alert fires on the wrong threshold. Fix the check,
# ? not the service — same split.

# * Skip local run. Chapter 14 practice done on Boot.dev.
