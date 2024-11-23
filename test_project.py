from project import create_sea
from project import create_mystery
from project import pass_turn


def test_create_sea():
    assert create_sea(3)==[["🌊","🌊","🌊"],["🌊","🌊","🌊"],["🌊","🌊","🌊"]]
    assert create_sea(4)==[["🌊","🌊","🌊","🌊"],["🌊","🌊","🌊","🌊"],["🌊","🌊","🌊","🌊"],["🌊","🌊","🌊","🌊"]]

def test_create_mystery():
    assert create_mystery(3)==[["❓","❓","❓"],["❓","❓","❓"],["❓","❓","❓"]]

def test_pass_turn():
    assert pass_turn("yes")==False
    assert pass_turn("pass")==True
