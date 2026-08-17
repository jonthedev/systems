# * None Return
# * If a function does not return a value, Python gives back None.
# * These three are the same result (None):

# ? def my_func():
# ?     print("I do nothing")
# ?     return None
# ?
# ? def my_func():
# ?     print("I do nothing")
# ?     return
# ?
# ? def my_func():
# ?     print("I do nothing")
# ?
# ? result = my_func()  # prints "I do nothing"
# ? print(result)       # None
# ?
# ? JS: a function with no return gives undefined.
# ? Python: None. That is why get_title had to return, not only print.
