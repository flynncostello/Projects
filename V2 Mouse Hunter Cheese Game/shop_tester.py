from shop import find_cheese_index

def test1():
    expected = (True, 2)
    actual = find_cheese_index("swiss")
    print(actual)
    assert expected == actual, "FAILED"
    print("PASSED")

if __name__ == "__main__":
    test1()
