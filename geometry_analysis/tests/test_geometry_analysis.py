"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys
import numpy as np


@pytest.fixture()
def water_molecule():
    name = 'water'
    symbols = ["H", "O", "H"]
    coordinates = np.array([[2, 0, 0], [0, 0, 0], [-2, 0, 0]])

    water = geometry_analysis.Molecule(name, symbols, coordinates)

    return water


def test_create_failure():

    name = 25
    symbols = ["H", "O", "H"]
    coordinates = np.zeros([3, 3])

    with pytest.raises(TypeError):
        water = geometry_analysis.Molecule(name, symbols, coordinates)


def test_molecule_set_coordinates(water_molecule):
    """Test that bond list is rebuilt when we reset coordinates."""

    num_bonds = len(water_molecule.bonds)

    assert num_bonds == 2

    new_coordinates = np.array([[5, 0, 0], [0, 0, 0], [-2, 0, 0]])
    water_molecule.coordinates = new_coordinates

    new_bonds = len(water_molecule.bonds)

    assert new_bonds == 1
    assert np.array_equal(new_coordinates, water_molecule.coordinates)


def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules


def test_calculate_distance():
    """Test the calculation distance function"""

    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])

    expected_distance = np.sqrt(2.)

    calculate_distance = geometry_analysis.calculate_distance(r1, r2)

    assert expected_distance == calculate_distance
    return


def test_calculate_angle_90():
    """Test the calculate angle function"""
    r1 = np.array([1, 0, 0])
    r2 = np.array([0, 0, 0])
    r3 = np.array([0, 1, 0])

    expected_angle = 90

    calculted_angle = geometry_analysis.calculate_angle(r1, r2, r3, degrees=True)

    assert expected_angle == calculted_angle


def test_calculate_angle_60():
    """Test the calculate angle function"""
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = 60

    calculted_angle = geometry_analysis.calculate_angle(r1, r2, r3, degrees=True)

    np.isclose(expected_angle,calculted_angle)


# We are gonna use decorators and merge the two test that runs both test for us.

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
    (np.array([1, 0, 0]), np.array([0, 0, 0]), np.array([0, 1, 0]), 90),
    (np.array([0, 0, -1]), np.array([0, 1, 0]), np.array([1, 0, 0]), 60)
])
def test_calculate_angle(p1, p2, p3, expected_angle):
    calculated_angle = geometry_analysis.calculate_angle(p1, p2, p3, degrees=True)

    assert np.isclose(expected_angle, calculated_angle)
