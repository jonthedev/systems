# * % is remainder after division, *not* a percent. Same symbol as JS.
# * 8 % 3 → 2   because 3*2=6, leftover 2.
# * Even: n % 2 == 0. Odd: n % 2 != 0  (leftover is 1).
# ?
# ? 7 % 2 → 1   (odd)
# ? 6 % 2 → 0   (even)
# ?
# ? range(0, num) is 0 .. num-1 (exclusive stop again).
# ? 0 is even, so it is not appended.
# ?
# ? JS: if (i % 2 !== 0) oddNumbers.push(i)
# ?
# ? Ops flavour: i % 3 == 0 → every 3rd host. Also wrap-around:
# ? hosts[i % len(hosts)]  when you run off the end of a list.

# * Assignment: if i is odd, append it. Return the list of odds.

def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        
        if i % 2 != 0:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers


print(get_odd_numbers(10))




