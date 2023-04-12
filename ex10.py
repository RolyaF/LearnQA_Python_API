class Ex10:
    phrase = input("Set a phrase: ")
    expected_amount = 15

    assert len(phrase) <= 15, f"Length of phrase is not equal {expected_amount}"
    print(f"Input phrase length: {len(phrase)}")