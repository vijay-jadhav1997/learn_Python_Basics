""" Comparison operators """

#? Comparison operators are used to compare two values.


def test_comparison_operators():
    """Comparison operators"""
    #? (==, !=, >, <, >=, <=)

    # Equal (==)
    number = 5
    print(f"{number} == 5 ==> {number == 5}")

    # Not equal (!=)
    number = 5
    print(f"{number} != 3 ==> {number != 3}")
    print(f"{number} != 5 ==> {number != 5}")

    # Greater than (>)
    number = 5
    print(f"{number} > 3 ==> {number > 3}")
    print(f"{number} > 5 ==> {number > 5}")
    print(f"{number} > 10 ==> {number > 10}")

    # Less than (<)
    number = 5
    print(f"{number} < 8 ==> {number < 8}")
    print(f"{number} < 5 ==> {number < 5}")
    print(f"{number} < 3 ==> {number < 3}")

    # Greater than or equal to (>=)
    number = 5
    print(f"{number} >= 5 ==> {number >= 5}")
    print(f"{number} >= 4 ==> {number >= 4}")
    print(f"{number} >= 10 ==> {number >= 10}")

    # Less than or equal to (<=)
    number = 5
    print(f"{number} <= 5 ==> {number <= 5}")
    print(f"{number} <= 5 ==> {number <= 6}")
    print(f"{number} <= 1 ==> {number <= 1}")