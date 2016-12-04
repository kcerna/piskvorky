import piskvorky as pis
import pytest


def test_vyhodnot():
    assert pis.vyhodnot("XXX----") == "X"
    assert pis.vyhodnot("000----") == "0"
    assert pis.vyhodnot("0--X---") == "-"
    assert pis.vyhodnot("00XX00X") == "!"



def test_tah():
    assert pis.tah("-----", 1, "x") == "-x---"

assert pis.tah("-----", 0, "x") == "x----"
