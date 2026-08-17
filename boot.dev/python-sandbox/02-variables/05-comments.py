# * Comments
# * Comments do nothing at runtime. The interpreter skips them.
# * They are notes for humans.

# ? Single line: # makes the rest of that line a comment.
# ? # speed is meters per second
# ? speed = 2

# * "Multi-line comments"
# * Python has no /* */ like JavaScript. Boot.dev shows triple quotes:

# ? """
# ? the code found below
# ? will print 'Hello, World!' to the console
# ? """
# ? print("Hello, World!")

# ? Triple quotes are a STRING, not a comment. If that block sits
# ? alone, Python builds the string and throws it away — it only
# ? looks like a comment. Real comments are #.

# * Why earlier files used # on every line
# ? Better Comments tags (# * / # ?) only paint comment lines.
# ? Inside """ they are just text in a string. We also wanted
# ? each line tagged, and we did not want fake comments.

# * Assignment
# ? Line 1 was meant to be a comment. The developer forgot #.

# the best_sword variable holds the value of the best sword in the game
best_sword = "scimitar"
print(best_sword)
