from project import BMR, totalexpenditure, Water

def test_BMR():
    assert BMR(70, 175, 25, 5) == 1673.75
    assert BMR(70, 175, 25, -161) == 1507.75

def test_totalexpenditure():
    assert totalexpenditure(1687.5, 0) == 1687.5 * 1.2
    assert totalexpenditure(1687.5, 1) == 1687.5 * 1.375
    assert totalexpenditure(1687.5, 2) == 1687.5 * 1.55
    assert totalexpenditure(1687.5, 3) == 1687.5 * 1.725
    assert totalexpenditure(1687.5, 4) == 1687.5 * 1.9

def test_Water():
    assert Water(70) == "2.450 l"

