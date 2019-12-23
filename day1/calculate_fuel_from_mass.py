"""Code to handle calculating mass according to day 1 function.

"""

# day 1 part 1
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


# day 1 part 2
def calculate_fuel_recursively(mass):
    """Calculates fuel requirements for a module accounting for the fact that fuel itself
     needs fuels.

    Args:
        mass: the mass of the module for which fuel requirements must be calculated.

    Returns:
        The fuel necessary for the module with mass 'mass', accounting for the fact that
    fuel itself needs fuel
    """
    fuel = calculate_fuel_from_mass(mass)
    if fuel < 0:
        return 0
    return calculate_fuel_recursively(fuel) + fuel


def calculate_total_fuel_recursively(filename):
    """Calculates the total fuel requirements for a list of module masses in file filename,
    accounting for fuel itself needing fuel.

    Args:
        filename: The name of the file containing module masses.

    Returns:
        The total fuel requirements for all the masses, accounting for the fuel's mass.
    """
    return sum([calculate_fuel_recursively(mass) for mass in read_mass_from_file(filename)])
