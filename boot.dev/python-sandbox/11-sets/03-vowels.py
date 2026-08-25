# * Walk the string char by char (for c in text). JS: for (const c of text)
# * Two answers: a *count* (every vowel, including repeats) and a *set*
# * (each distinct letter once). "aaa" → count 3, set {'a'}
# ?
# ? A and a are different. Add both to the allowed bag.
# ?
# ? if c in vowels  is the set-shaped check (one `in`, not ten ==).
# ? vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
# ? Your two if-chains do the same job, just louder.
# ?
# ? .add() on a set: first time it lands, second time is a no-op.
# ? += 1 always, even when the set already had that letter.
# ?
# ? Drop the debug prints before a Boot.dev submit.
# ?
# ? Ops flavour: count how many times a status letter appears in a
# ? code, and which distinct letters showed up.

# * Assignment: vowel count (all hits) + set of unique vowels found.

from typing import Any


def count_vowels(text):
    vowel_count = 0
    vowel_set = set()
    for c in text:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            vowel_count += 1
            vowel_set.add(c)
        if c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
            vowel_count += 1
            vowel_set.add(c)
    

    return vowel_count, vowel_set


print(count_vowels("Aaa Eee hello"))