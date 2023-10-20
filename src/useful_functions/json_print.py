def json_print(tree, level=0):
    if isinstance(tree, dict):
        print("{")

        for key, value in tree.items():
            print("  " * (level + 1) + f'"{key}": ', end="")
            json_print(value, level + 1)

        print("  " * level + "}")

    elif isinstance(tree, list):
        print("[")

        for element in tree:
            json_print(element, level + 1)
            if element != tree[-1]:
                print(",")

        print("  " * level + "]")

    elif isinstance(tree, str):
        print(f'"s"')

    else:
        print(tree)
