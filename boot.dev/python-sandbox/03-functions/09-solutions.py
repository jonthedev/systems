# * Solutions
# * Boot.dev hides an instructor solution behind XP / a seer stone
# * until you finish. After that, comparing is free and useful.
# * Use it sparingly — once a chapter if you are stuck, not as the
# * first move. Discord before spoilers.

# * Assignment
# ? Convert hours to seconds. 60 seconds in a minute, 60 minutes
# ? in an hour → 3600 seconds per hour. Return that, do not print.

def hours_to_seconds(hours):
    seconds_per_minute = 60
    seconds_per_hour = 60 * seconds_per_minute
    return hours * seconds_per_hour


# ? Don't touch below this line
def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)
