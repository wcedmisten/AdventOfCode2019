"""Code to handle calculating mass according to day 1 function.

"""

def calculate_fuel_from_mass(mass):
    """Calculates fuel requirement for space ship, according to the day 1 formula.

    Args:
        mass: the mass of the module for which fuel requirements must be calculated.

    Returns:
        The fuel necessary for the module with mass 'mass'.
    """
    return int(mass / 3) - 2

def read_mass_from_file(filename):
    """Grabs a list of module masses from a file, given that each is on a new line.

    Args:
        filename: The name of the file containing module masses.

    Returns:
        The list of module masses found in the file.
    """
    masses = []
    with open(filename) as mass_file:
        for num in mass_file:
            masses.append(int(num))

    return masses

def calculate_total_fuel(filename):
    """Calculates the total fuel requirements for a list of module masses in file filename.

    Args:
        filename: The name of the file containing module masses.

    Returns:
        The total fuel requirements for all the masses.
    """
    return sum([calculate_fuel_from_mass(mass) for mass in read_mass_from_file(filename)])
