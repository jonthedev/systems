# * Bitwise OR:  |
# * Same rule as logical `or`, but per *bit column*.
# * A column is 1 if *either* input has a 1 there (union of bits).
# ?
# ?   0101   (5)
# ? | 0111   (7)
# ?   0111   (7)     any column that was 1 in A *or* B
# ?
# ?   0101   (5)
# ? | 0010   (2)
# ?   0111   (7)
# ?
# ? 1 | 1 → 1    1 | 0 → 1    0 | 0 → 0
# ?
# ? Pair with last lesson:
# ?   &  = keep bits that are on in *both*  (check / mask)
# ?   |  = turn on bits that are on in *either*  (combine / grant)
# ?
# ? JS trap:  || is logical.  | is bitwise.
# ?          Same split in Python:  or  vs  |

# * Why ops cares: stack flags into one number.
# * chmod rwx:  4 | 2 | 1  →  7  (all three bits on).

# * Guild: | merges everyone's permissions (Jack 0b1000 | Jill 0b0100 → 0b1100).
# ? can_invite          0b1000
# ? can_kick            0b0100
# ? can_enter_dungeon   0b0010
# ? can_surrender       0b0001

# * Assignment: OR all four members together ( | chains).

def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    return glorfindel | galadriel | elendil | elrond
