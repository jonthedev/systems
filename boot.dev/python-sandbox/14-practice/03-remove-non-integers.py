# * Filter: walk the list, keep only real ints. Build a *new* list — don't
# * mutate nums. type() tells you what something *is*, not how it looks.
# ?
# ? type(1) is int              True
# ? type("1") is str            True   # looks numeric, still a string
# ? type(1.0) == float          True   # 1.0 is not an int
# ? type("seventy-six") == int  False
# ?
# ? ["1", 1, "3", "400", 4, 500]  →  [1, 4, 500]
# ? "1" and "400" stay out. We do *not* int("1") — that would convert, not filter.
# ?
# ? Empty result list outside the loop. if type is int → append. Else skip.
# ? Original nums is unchanged (same idea as not editing a source list in place).
# ?
# ? `is` vs `==` on types: Boot.dev showed both. For a class object they match.
# ? `is` = same object. `==` = equal value. Fine here either way.
# ?
# ? TS: typeof 1 === "number" — but JS doesn't split int/float.
# ?     Number.isInteger(1) vs Number.isInteger(1.0)
# ? Python: type(1) is int, type(1.0) is float.
# ?
# ? Ops flavour: a mixed config list ["80", 80, 443] — keep only real ints
# ? so you don't treat the string "80" as a port number by accident.

# * Assignment: return a new list of ints only. Don't change nums.

def remove_nonints(nums: list[object]) -> list[int]:
    list_no_ints: list[int] = []

    for num in nums:
        if(type(num) is int):
            list_no_ints.append(num)

    return list_no_ints


print(remove_nonints(["1", 1, "3", "400", 4, 500]))
