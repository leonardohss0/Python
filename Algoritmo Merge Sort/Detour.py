def test(title: str, value, expected) -> None:
    print("[" + title + "] " + str(value))
    if value == expected:
        print("Pass")
    else:
        print("Fail")
