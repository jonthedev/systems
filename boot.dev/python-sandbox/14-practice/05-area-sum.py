# * Same accumulator as number_sum. Each pass: area = height * width, add that.
# * Each rectangle is a dict with "height" and "width" keys, not a tuple.
# ?
# ? {"height": 3, "width": 5}  →  3 * 5 = 15
# ? Two rects: 15 + (2 * 4) = 23
# ? [] → 0  (loop never runs)
# ?
# ? list[dict[str, int]]  read outside-in:
# ?   a list of  dicts  whose keys are str and values are int
# ?
# ? rectangle["height"]  lookup by name, not [0].
# ? A tuple version would be (h, w) and you'd write rectangle[0] * rectangle[1].
# ? Dict is clearer when the fields have names.
# ?
# ? TS: { height: number; width: number }[]
# ?     total += r.height * r.width   (dot vs Python ["height"])
# ?
# ? Ops flavour: each VM is { "vcpus": n, "ram_gb": m }. Same walk:
# ? look up two fields, multiply or add, keep a running total.

# * Assignment: sum height*width for every rectangle dict.

def area_sum(rectangles: list[dict[str, int]]) -> int:

    total = 0
    for rectangle in rectangles:
        total += rectangle["height"] * rectangle["width"]
    return total


print(area_sum([{"height": 3, "width": 5}, {"height": 2, "width": 4}]))
print(area_sum([]))
