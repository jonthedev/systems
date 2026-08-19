# * Stack trace (traceback)
# * When Python dies, it prints the path it took through your files
# * and the last line is the actual error. Read from the bottom:
# ?   error type  →  the line  →  which file
# * JS: same idea as a Chrome red stack, just uglier in the terminal.
# *
# * This lesson's errors (on purpose):
# * 1. IndentationError — line used 6 spaces; Python wants 4 (or one tab).
# * 2. SyntaxError — f-string missing the closing quote.
# * The "<string>" / pyodide path is Boot.dev's browser Python. Ignore it.
# * Look at main.py and the line number they name.

# * Assignment: fix indent, then close the string. No logic bug.

def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg
