# * Factorial = *product* of 1 through n. Same walk as number_sum, but multiply.
# * ! is math notation, not a Python operator. Use a loop.
# ?
# ? 1! = 1
# ? 2! = 2 * 1           = 2
# ? 3! = 3 * 2 * 1       = 6
# ? 5! = 5 * 4 * 3 * 2 * 1 = 120
# ? 0! = 1   # by definition. Also: empty loop, start value survives.
# ?
# ? Start result at 1, not 0.  0 * anything = 0  would wipe the answer.
# ? Empty product (0!) is 1, the same way an empty *sum* is 0.
# ?
# ? range(1, num + 1) includes num. Same n+1 trick as number_sum.
# ? *=  is in-place multiply (chapter 6), twin of +=.
# ?
# ? JS: let result = 1; for (let i = 1; i <= num; i++) result *= i
# ? No factorial operator there either. Math.factorial is a later library.
# ?
# ? Ops flavour: n! = how many orders you can line up n unique hosts.
# ? 0 hosts → 1 empty order, not zero.

# * Assignment: return n! with a multiply loop. 0! is 1.

def factorial(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


print(factorial(0))
print(factorial(1))
print(factorial(5))
