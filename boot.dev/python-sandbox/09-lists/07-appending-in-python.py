# * append — add one item to the *end* of the list.
# * Common pattern: start empty, fill in a loop, return the list.
# * JS: arr.push(item). Python: list.append(item)
# ?
# ? cards = []
# ? cards.append("nvidia")
# ? cards.append("amd")
# ? # ["nvidia", "amd"]
# ?
# ? range(0, num_of_users) is 0 .. num_of_users-1 (exclusive stop again).
# ? range(num_of_users) is the same thing — 0 is the default start.
# ?
# ? Ops flavour: hosts = []; for name in new_boxes: hosts.append(name)

# * Assignment: each lap, append i as a unique player id.

def generate_user_list(num_of_users):
    player_ids = []

    for i in range(0, num_of_users):
        player_ids.append(i)

    return player_ids


print(generate_user_list(5))