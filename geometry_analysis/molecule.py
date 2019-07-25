"""
molecule.py
TA python package for the MolSSI Software Summer School.

Handles the primary functions
"""

"""
molecule.py
A python package for the MolSSI Software Summer School.

Contains a molecule class
"""

import numpy as np

def calculate_distance(rA, rB):
    """Calculate the distance between points A and B.
    
    Parameters
    ----------
    rA : numpy array
        The x, y, z coordinates of point A
    rB : numpy array
        The x, y, z coordinates of point B
    
    Returns
    -------
    distance : float
        The distance between points A and B.
    
    Examples
    --------
    >>> calculate_distance(np.array([0, 0, 0], [0, 0.1, 0]))
    0.1
    """
    dist_vec = (rA-rB)
    distance = np.linalg.norm(dist_vec)
    return distance

def calculate_angle(rA, rB, rC, degrees=False):
    """Calculate angle between points A, B, and C
    
    Parameters
    ----------
    rA : numpy array
        The x, y, z coordinates of point A
    rB : numpy array
        The x, y, z coordinates of point B
    degrees : bool, optional
        Return the calculated angle in degrees.
    
    Returns
    -------
    angle : float
        The distance between points A and B.
    """
    AB = rB - rA
    BC = rB - rC
    
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB)*np.linalg.norm(BC)))
    
    if degrees: 
        return np.degrees(theta)
    else:
        return theta

class Molecule:
    def __init__(self, name, symbols, coordinates):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError("Name is not a string.")
        
        self.symbols = symbols
        self.coordinates = coordinates
        self.bonds = self.build_bond_list()
    
    @property
    def num_atoms(self):
        return len(self.coordinates)
    
    @property
    def coordinates(self):
        return self._coordinates
    
    @coordinates.setter
    def coordinates(self, new_coordinates):
        self._coordinates = new_coordinates
        self.bonds = self.build_bond_list()

    
    def build_bond_list(self, max_bond=2.93, min_bond=0):
        """
        Build a list of bonds based on a distance criteria.

        Atoms within a specified distance of one another will be considered bonded.

        Parameters
        ----------
        max_bond : float, optional

        min_bond : float, optional

        Returns
        -------
        bond_list : list
            List of bonded atoms. Returned as list of tuples where the values are the atom indices.
        """
        
        bonds = {}
        
        for atom1 in range(self.num_atoms):
            for atom2 in range(atom1, self.num_atoms):
                distance = calculate_distance(self.coordinates[atom1], self.coordinates[atom2])
                
                if distance > min_bond and distance < max_bond:
                    bonds[(atom1, atom2)] = distance
        
        return bonds
    

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    pass
