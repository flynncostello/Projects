from shop import buy_cheese

def test01():
    gold = 125
    actual_output = buy_cheese(gold)
    expected_output = (110, (1, 0, 1))
    assert expected_output == actual_output, "TEST 01 FAILED"
    print("TEST 01 PASSED")

def test02():
    gold = 125
    actual_output = buy_cheese(gold)
    expected_output = (0, (0, 0, 0))
    assert expected_output == actual_output, "TEST 02 FAILED"
    print("TEST 02 PASSED")

def test03():
    gold = 140
    actual_output = buy_cheese(gold)
    expected_output = (0, (0, 0, 0))
    assert expected_output == actual_output, "TEST 03 FAILED"
    print("TEST 03 PASSED")

def test04():
    gold = 155
    actual_output = buy_cheese(gold)
    expected_output = (0, (0, 0, 0))
    assert expected_output == actual_output, "TEST 04 FAILED"
    print("TEST 04 PASSED")

def test05():
    gold = 165
    actual_output = buy_cheese(gold)
    expected_output = (0, (0, 0, 0))
    assert expected_output == actual_output, "TEST 05 FAILED"
    print("TEST 05 PASSED")

def test06():
    gold = 175
    actual_output = buy_cheese(gold)
    expected_output = (100, (0, 0, 1))
    assert expected_output == actual_output, "TEST 06 FAILED"
    print("TEST 06 PASSED")

def test07():
    gold = 185
    actual_output = buy_cheese(gold)
    expected_output = (0, (0, 0, 0))
    assert expected_output == actual_output, "TEST 07 FAILED"
    print("TEST 07 PASSED")

def test08():
    gold = 195
    actual_output = buy_cheese(gold)
    expected_output = (0, (0, 0, 0))
    assert expected_output == actual_output, "TEST 08 FAILED"
    print("TEST 08 PASSED")



def main():
    print("TEST 1:\n")
    test01()
    print()
    print("TEST 2:\n")
    test02()
    print()
    print("TEST 3:\n")
    test03()
    print()
    print("TEST 4:\n")
    test04()
    print()
    print("TEST 5:\n")
    test05()
    print()
    print("TEST 6:\n")
    test06()
    print()
    print("TEST 7:\n")
    test07()
    print()
    print("TEST 8:\n")
    test08()

if __name__ == "__main__":
    main()







