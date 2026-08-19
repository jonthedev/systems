# * Floor division: //
# * Divide, then round *down* to a whole number (not "chop toward zero").
# ?
# ? 8 // 3   →  2     (8 / 3 is 2.666…, down to 2)
# ? 11 // 2  →  5     (11 / 2 is 5.5, down to 5)
# ? -7 // 3  →  -3    ( -7 / 3 is -2.333…, down is -3, not -2)
# ?
# ? JS: Math.floor(8 / 3) is the same idea.
# ?     Math.trunc(8 / 3) is *not* — trunc chops toward 0.
# ?     That difference shows up on negatives: Math.trunc(-2.33) is -2.

# * Q: 11 // 2 ?
# * A: 5
