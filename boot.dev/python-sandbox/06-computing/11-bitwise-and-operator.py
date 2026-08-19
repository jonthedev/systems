# * Bitwise AND:  &
# * Same rule as logical `and`, but per *bit column*, not the whole value.
# * 1 is True, 0 is False. Both columns must be 1 to keep a 1.
# ?
# ?   0101   (5)
# ? & 0111   (7)
# ?   0101   (5)     only columns that were 1 in *both*
# ?
# ?   0101   (5)
# ? & 0010   (2)
# ?   0000   (0)     no column was 1 in both
# ?
# ? 1 & 1 → 1    1 & 0 → 0    0 & 0 → 0
# ?
# ? JS trap:  && is logical (true/false).  & is bitwise (per bit).
# ?          Same split in Python:  and  vs  &
# ?          5 && 7  is 7 (truthy).  5 & 7  is 5 (bits).

# * Why ops cares: flags packed into one number.
# * Linux chmod is this: r=4 w=2 x=1.  5 is r-x (101). Check a bit with &.

# * Guild permissions (one bit each, 0b means binary):
# ? can_create_guild  0b1000
# ? can_review_guild  0b0100
# ? can_delete_guild  0b0010
# ? can_edit_guild    0b0001
# ?
# ? user 0b0101  = review + edit
# ? Check review:  0b0101 & 0b0100  →  0b0100  (that bit is on)
# ? Check create:  0b0101 & 0b1000  →  0b0000  (that bit is off)

# * Assignment: AND the user's bits with each flag, return what remains.

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    return user_permissions & can_create_guild


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild


def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild


def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild
