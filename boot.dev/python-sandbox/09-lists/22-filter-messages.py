# * Nested no-index loops: outer = each chat line, inner = each word.
# * split()  string → list of words (default: split on spaces). JS: .split(" ")
# * " ".join(list)  glue words back. Called on the *delimiter*, list is the arg.
# * JS is the other way around: goodWords.join(" ")
# ?
# ? Filter: "dang" → count it. Anything else → keep it (append).
# ? Two new lists, same order: cleaned line i matches count i.
# ?
# ? "dang it bobby!" → ["dang", "it", "bobby!"] → "it bobby!", count 1
# ?
# ? Original messages stay put. return a, b  is a tuple.
# ?
# ? This is the indexed version without i and j — you never needed the numbers.
# ?
# ? JS: messages.map(m => m.split(" ").filter(w => w !== "dang"))
# ?
# ? Ops flavour: strip a banned token from log lines, count drops per line.

# * Assignment: drop "dang" from each message; return cleaned lines + counts.

data = ['darn it', "this dang thing won't work", 'lets fight one on one']

def filter_messages(messages):
    filtered_messages = []
    dang_count = []

    for message in messages:
        good_words = []
        bad_word_count = 0

        for word in message.split():
         
            if (word == 'dang'):
                bad_word_count += 1
            else:
                good_words.append(word)

        sentence = " ".join(good_words)
        filtered_messages.append(sentence)
        dang_count.append(bad_word_count)
        
    return filtered_messages, dang_count

print(filter_messages(data))