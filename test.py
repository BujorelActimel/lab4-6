from functionalitati import *
from apartament import Apartament
import pytest


def compare_apartments(ap1, ap2):
    return ap1.getApartmentNumber() == ap2.getApartmentNumber() and ap1.costs == ap2.costs


# test Apartment methods
def test_getApartmentNumber():
    test_apartm = Apartament(0)
    assert test_apartm.getApartmentNumber() == 0


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


def test_getCost():
    test_apartm = Apartament(0)
    test_apartm.addCost("apa", 100)
    assert test_apartm.getCost("apa") == 100
    assert test_apartm.getCost("canal") == 0


def test_copy():
    test_apartm = Apartament(0)
    assert compare_apartments(test_apartm, Apartament(0))

    test_apartm.addCost("apa", 100)
    assert test_apartm.copy().costs == {"apa": 100}


# test Functionalities
def test_exists():
    test_building = [Apartament(0), Apartament(1), Apartament(10)]
    assert exists(test_building, 0)
    assert exists(test_building, 1)
    assert exists(test_building, 10)
    assert not exists(test_building, 7)


def test_get_apartment():
    test_building = [Apartament(1), Apartament(2)]
    test_building[0].addCost("apa", 100)

    test_ap = Apartament(1)
    test_ap.addCost("apa", 100)

    assert compare_apartments(get_apartment(test_building, 1), test_ap)
    assert compare_apartments(get_apartment(test_building, 2), Apartament(2))
    assert compare_apartments(get_apartment(test_building, 0), Apartament(0))


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


def test_undo():
    ap1 = Apartament(1)
    ap2 = Apartament(2)
    ap3 = Apartament(3)
    ap1.addCost("apa", 100)
    ap2.addCost("canal", 200)
    ap3.addCost("intretinere", 280)

    prev_states = [[ap1], [ap1, ap2]]
    
    current_building = [ap1, ap2, ap3]

    current_building = undo(prev_states, current_building)
    assert current_building == [ap1, ap2]

    current_building = undo(prev_states, current_building)
    assert current_building == [ap1]

    current_building = undo(prev_states, current_building)
    assert current_building == []


def test_delete_costs_of_type():
    ap1 = Apartament(1)
    ap1.addCost("apa", 200)
    ap1.addCost("canal", 120)
    ap2 = Apartament(2)
    ap2.addCost("apa", 100)
    building = [ap1, ap2]
    delete_costs_of_type(building, "apa")

    test_ap1 = Apartament(1)
    test_ap1.addCost("canal", 120)
    test_ap2 = Apartament(2)

    assert compare_apartments(ap1, test_ap1)
    assert compare_apartments(ap2, test_ap2)


def test_delete_costs_less_than_sum():
    ap1 = Apartament(1)
    ap1.addCost("apa", 200)
    ap1.addCost("canal", 120)
    ap2 = Apartament(2)
    ap2.addCost("apa", 100)
    building = [ap1, ap2]
    delete_costs_less_than_sum(building, 200)

    test_ap1 = Apartament(1)
    test_ap1.addCost("apa", 200)
    test_ap2 = Apartament(2)

    assert compare_apartments(ap1, test_ap1)
    assert compare_apartments(ap2, test_ap2)
