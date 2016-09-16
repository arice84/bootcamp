import pytest
import TTD

def test_n_neg():
    assert TTD.n_neg('E') == 1
    assert TTD.n_neg('D') == 1
    assert TTD.n_neg('') == 0
    assert TTD.n_neg('ACKLWTTAE') == 1
    assert TTD.n_neg('DEDE') == 4
    assert TTD.n_neg('acklwttae') == 1

    pytest.raises(RuntimeError, "TTD.n_neg('Z')")

    return None
