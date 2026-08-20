# * Guard clauses: invert the happy path
# * Don't nest "age ok AND working AND time ok". Fail early instead:
# * if a rule is broken, return False. If you survive all checks, True.
# ?
# ? Serve only if ALL of:
# ?   age >= 21, bartender working (on_break is False), time 5–10 inclusive
# ?
# ? Fail if:
# ?   age < 21
# ?   on_break          (True = on break = not working)
# ?   time < 5 or time > 10    (5 and 10 still serve)
# ?
# ? Nested (harder to read) vs early returns (this file):
# ? if age_ok:
# ?     if not on_break:
# ?         if time_ok:
# ?             return True
# ? return False
# ?
# ? `if on_break:` is enough. `if on_break == True:` works but is redundant.
# ? JS: same early-return style.  if (onBreak) return false
# ?
# ? Ops flavour: if disk_full: abort. if not healthy: abort. then deploy.

def should_serve_customer(customer_age, on_break, time):
    if customer_age < 21:
        return False
    if on_break:
        return False
    if time < 5 or time > 10:
        return False
    return True
