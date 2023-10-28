from functionalitati import *
from apartament import Apartament
import pytest

def test_exists():
    test_building = [Apartament(0), Apartament(1), Apartament(10)]
    assert exists(test_building, 0)
    assert exists(test_building, 1)
    assert exists(test_building, 10)
    assert not exists(test_building, 7)


def test_addCost():
    test_apartm = Apartament(0)
    test_apartm.addCost("apa", 100)
    assert test_apartm.costs == {
        "apa": 100
    }
    test_apartm.addCost("canal", 200)
    assert test_apartm.costs == {
        "apa": 100, 
        "canal": 200
    }


def test_deleteAllCosts():
    test_apartment = Apartament(0)
    test_apartment.addCost("apa", 100)
    test_apartment.deleteAllCosts()
    
    assert test_apartment.costs == {}


def test_deleteCost():
    test_apartment = Apartament(0)
    test_apartment.addCost("apa", 100)
    test_apartment.addCost("canal", 120)
    test_apartment.deleteCost("apa")
    assert test_apartment.costs == {"canal": 120}

    test_apartment.deleteCost("canal")
    assert test_apartment.costs == {}

    with pytest.raises(KeyError):
        test_apartment.deleteCost("gunoi") # nu exista
    assert test_apartment.costs == {}


def test_totalCosts():
    test_apartment = Apartament(0)
    test_apartment.addCost("apa", 200)
    assert test_apartment.totalCosts() == 200

    test_apartment.addCost("canal", 100)
    assert test_apartment.totalCosts() == 300

    test_apartment.addCost("whatever", 50) 
    assert test_apartment.totalCosts() == 350

    test_apartment.deleteCost("apa")
    assert test_apartment.totalCosts() == 150

    test_apartment.deleteAllCosts()
    assert test_apartment.totalCosts() == 0


def test_delete_from_range():
    test_ap1 = Apartament(1)
    test_ap2 = Apartament(2)
    test_ap3 = Apartament(3)

    test_ap1.addCost("apa", 100)
    test_ap2.addCost("apa", 100)
    test_ap3.addCost("apa", 100)

    test_building = [test_ap1, test_ap2, test_ap3]
    delete_from_range(test_building, 2, 10)

    assert test_building[0].costs == {"apa": 100}
    assert test_building[1].costs == {}
    assert test_building[2].costs == {}
