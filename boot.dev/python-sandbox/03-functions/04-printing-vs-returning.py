# * Printing vs returning
# * Tests often print your return value, so print() and return can
# * look interchangeable. They are not.

# ? print(): writes to the console. Does not hand a value back.
# ?          printed_alchemy = print_alchemy()  →  None
# ?
# ? return:  ends the function and gives a value to the caller.
# ?          Does not print unless someone later print()s it.
# ?
# ? JS: console.log vs return — same split.
# ? Ops: print is a log line. return is the result the next step uses.

# * Print to debug, then remove it. Leftover print() breaks Boot.dev
# * tests (extra console output) and clutters production logs.

# * Assignment
# ? get_title should return the title, not print it.

def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title


# ? Don't touch below this line
def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")
