# * Mount rental — early return, no else (the bonus)
# * If used time meets or exceeds purchased time → overtime.
# * >=  so equal time is already expired (not "one more minute free").
# ?
# ? if time_used >= time_purchased:
# ?     return "overtime charged"
# ? return "no charges yet"
# ?
# ? Same pattern as 05 (swords) and 11 (guard clauses):
# ? handle the special case, then the default.
# ? else: would work; Python style often skips it after a return.

def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"