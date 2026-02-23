def grocery_store(**kwargs):
    result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))

    receipt = []
    for product, quantity in result:
        receipt.append(f"{product}: {quantity}")

    return "\n".join(receipt)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
