"""Input cipher key string, get user input on route direction as dict value."""

col_order = """1 3 4 2"""
key = {}
cols = [int(i) for i in col_order.split()]
for col in cols:
    while True:
        key[col] = input(
            f"Direction to read Column {col} (u = up, d = down): ".lower()
        )
        if key[col] in ['u', 'd']:
            break
        else:
            print("Input should be 'u' or 'd'")

    print(f"{col}, {key[col]}")
