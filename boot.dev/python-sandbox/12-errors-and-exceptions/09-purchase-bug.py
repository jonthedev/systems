# * Same rule: raise here, do *not* except in this function. Tests catch it.
# * The bug was selling when gold < price. Raising stops that fake purchase.
# ?
# ? enough gold  → return gold_available - price  (what's left)
# ? not enough   → raise Exception("not enough gold")
# ?
# ? Guard-first shape (same logic):
# ? if gold_available < price:
# ?     raise Exception("not enough gold")
# ? return gold_available - price
# ?
# ? JS: throw new Error("not enough gold") in the helper, catch at checkout.
# ?
# ? Ops flavour: refuse a deploy if disk is under the minimum.
# ? Don't write the files then pretend it worked.

# * Assignment: too poor → raise. Else return remaining gold.

def purchase_item(price, gold_available):
    if gold_available >= price:
        gold_available = gold_available - price
        return gold_available
    else:
        raise Exception("not enough gold")


print(purchase_item(50, 80))
try:
    purchase_item(50, 20)
except Exception as e:
    print(e)