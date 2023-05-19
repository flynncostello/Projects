from game import change_cheese

def test01():
    name = "Flynn"
    trap = "Cardboard and Hook Trap"
    cheese_list = [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]
    e_flag = False
    actual_output = change_cheese(name, trap, cheese_list, e_flag)
    expected_output = (True, "Cheddar")
    assert expected_output == actual_output, "TEST 01 FAILED"
    print("TEST 01 PASSED")

def test02():
    name = "Dan"
    trap = "Cardboard and Hook Trap"
    cheese_list = [["Cheddar", 0], ["Marble", 1], ["Swiss", 0]]
    e_flag = False
    actual_output = change_cheese(name, trap, cheese_list, e_flag)
    expected_output = (True, "Marble")
    assert expected_output == actual_output, "TEST 02 FAILED"
    print("TEST 02 PASSED")

def test03():
    name = "Joe"
    trap = "Cardboard and Hook Trap"
    cheese_list = [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]
    e_flag = False
    actual_output = change_cheese(name, trap, cheese_list, e_flag)
    expected_output = (False, None)
    assert expected_output == actual_output, "TEST 03 FAILED"
    print("TEST 03 PASSED")

def test04():
    name = "Zac"
    trap = "Cardboard and Hook Trap"
    cheese_list = [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]
    e_flag = False
    actual_output = change_cheese(name, trap, cheese_list, e_flag)
    expected_output = (False, None)
    assert expected_output == actual_output, "TEST 04 FAILED"
    print("TEST 04 PASSED")

def test05():
    name = "Daniel"
    trap = "Cardboard and Hook Trap"
    cheese_list = [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]
    e_flag = False
    actual_output = change_cheese(name, trap, cheese_list, e_flag)
    expected_output = (False, None)
    assert expected_output == actual_output, "TEST 05 FAILED"
    print("TEST 05 PASSED")

def test06():
    name = "Sophie"
    trap = "Cardboard and Hook Trap"
    cheese_list = [["Cheddar", 1], ["Marble", 0], ["Swiss", 0]]
    e_flag = False
    actual_output = change_cheese(name, trap, cheese_list, e_flag)
    expected_output = (True, "Cheddar") 
    assert expected_output == actual_output, "TEST 06 FAILED"
    print("TEST 06 PASSED")


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

if __name__ == "__main__":
    main()








