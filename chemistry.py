# Tiros Anibal Lopez Week 4 CSE 111
# create the periodic table
from formula import parse_formula
#Exceeding the Requirements
def find_known_moleculed_dict():
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water"
    }
    return known_molecules_dict


def make_periodic_table():
    periodic_table_dict = {
        # [atomic_symbol, name, atomic mass]
        "Ac":["Actinium",227],
        "Ag":["Silver",107.8682],
        "Al":["Aluminum",26.9815386],
        "Ar":["Argon",39.948],
        "As":["Arsenic",74.9216],
        "At":["Astatine",210],
        "Au":["Gold",196.966569],
        "B":["Boron",10.811],
        "Ba":["Barium",137.327],
        "Be":["Beryllium",9.012182],
        "Bi":["Bismuth",208.9804],
        "Br":["Bromine",79.904],
        "C":["Carbon",12.0107],
        "Ca":["Calcium",40.078],
        "Cd":["Cadmium",112.411],
        "Ce":["Cerium",140.116],
        "Cl":["Chlorine",35.453],
        "Co":["Cobalt",58.933195],
        "Cr":["Chromium",51.9961],
        "Cs":["Cesium",132.9054519],
        "Cu":["Copper",63.546],
        "Dy":["Dysprosium",162.5],
        "Er":["Erbium",167.259],
        "Eu":["Europium",151.964],
        "F":["Fluorine",18.9984032],
        "Fe":["Iron",55.845],
        "Fr":["Francium",223],
        "Ga":["Gallium",69.723],
        "Gd":["Gadolinium",157.25],
        "Ge":["Germanium",72.64],
        "H":["Hydrogen",1.00794],
        "He":["Helium",4.002602],
        "Hf":["Hafnium",178.49],
        "Hg":["Mercury",200.59],
        "Ho":["Holmium",164.93032],
        "I":["Iodine",126.90447],
        "In":["Indium",114.818],
        "Ir":["Iridium",192.217],
        "K":["Potassium",39.0983],
        "Kr":["Krypton",83.798],
        "La":["Lanthanum",138.90547],
        "Li":["Lithium",6.941],
        "Lu":["Lutetium",174.9668],
        "Mg":["Magnesium",24.305],
        "Mn":["Manganese",54.938045],
        "Mo":["Molybdenum",95.96],
        "N":["Nitrogen",14.0067],
        "Na":["Sodium",22.98976928],
        "Nb":["Niobium",92.90638],
        "Nd":["Neodymium",144.242],
        "Ne":["Neon",20.1797],
        "Ni":["Nickel",58.6934],
        "Np":["Neptunium",237],
        "O":["Oxygen",15.9994],
        "Os":["Osmium",190.23],
        "P":["Phosphorus",30.973762],
        "Pa":["Protactinium",231.03588],
        "Pb":["Lead",207.2],
        "Pd":["Palladium",106.42],
        "Pm":["Promethium",145],
        "Po":["Polonium",209],
        "Pr":["Praseodymium",140.90765],
        "Pt":["Platinum",195.084],
        "Pu":["Plutonium",244],
        "Ra":["Radium",226],
        "Rb":["Rubidium",85.4678],
        "Re":["Rhenium",186.207],
        "Rh":["Rhodium",102.9055],
        "Rn":["Radon",222],
        "Ru":["Ruthenium",101.07],
        "S":["Sulfur",32.065],
        "Sb":["Antimony",121.76],
        "Sc":["Scandium",44.955912],
        "Se":["Selenium",78.96],
        "Si":["Silicon",28.0855],
        "Sm":["Samarium",150.36],
        "Sn":["Tin",118.71],
        "Sr":["Strontium",87.62],
        "Ta":["Tantalum",180.94788],
        "Tb":["Terbium",158.92535],
        "Tc":["Technetium",98],
        "Te":["Tellurium",127.6],
        "Th":["Thorium",232.03806],
        "Ti":["Titanium",47.867],
        "Tl":["Thallium",204.3833],
        "Tm":["Thulium",168.93421],
        "U":["Uranium",238.02891],
        "V":["Vanadium",50.9415],
        "W":["Tungsten",183.84],
        "Xe":["Xenon",131.293],
        "Y":["Yttrium",88.90585],
        "Yb":["Ytterbium",173.054],
        "Zn":["Zinc",65.38],
        "Zr":["Zirconium",91.224]
    }
    return periodic_table_dict


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    # Indexes for inner lists in the periodic table
    NAME_INDEX = 0
    ATOMIC_MASS_INDEX = 1
    # Indexes for inner lists in a symbol_quantity_list
    SYMBOL_INDEX = 0
    QUANTITY_INDEX = 1
    
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """

    total_molar_mass = 0
    
    for element in symbol_quantity_list:
 
        p_element = element[SYMBOL_INDEX]
        atoms = element[QUANTITY_INDEX]
        mass_info = periodic_table_dict[p_element]
        a_mass = mass_info[QUANTITY_INDEX]
        
        #formula
        molar_mass = atoms * a_mass
        total_molar_mass += molar_mass
        
        # Do the following for each inner list in the
        # compound symbol_quantity_list:
            # Separate the inner list into symbol and quantity.
            # Get the atomic mass for the symbol from the dictionary.
            # Multiply the atomic mass by the quantity.
            # Add the product into the total molar mass.
        # Return the total molar mass.
    return total_molar_mass

def get_formula_name(formula, known_molecules_dict):
    
    if formula in known_molecules_dict:
        formula_name = known_molecules_dict[formula]
        return formula_name
    else:
        print("Formula is not common")

def main():
    # Get a chemical formula for a molecule from the user.
    # Get the mass of a chemical sample in grams from the user.
    # Call the make_periodic_table function and
    # store the periodic table in a variable.
    # Call the parse_formula function to convert the
    # chemical formula given by the user to a compound
    # list that stores element symbols and the quantity
    # of atoms of each element in the molecule.
    # Call the compute_molar_mass function to compute the
    # molar mass of the molecule from the compound list.
    # Compute the number of moles in the sample.
    # Print the molar mass.
    # Print the number of moles.
     
    #Receive the inputs from users    
    formula = input("What is the Molecule Formula? ")
    sample = float(input("What is the Mass of the chemical sample (grams?? "))
    periodic_table_dict = make_periodic_table()
    known_molecules_dict = find_known_moleculed_dict()
    
    # print(periodic_table_dict)
    symbol_quantity_list = parse_formula(formula,periodic_table_dict)
    molar_mass= compute_molar_mass(symbol_quantity_list, periodic_table_dict)
    #calule the number of moles - formula
    number_of_moles = sample / molar_mass
    formula_name = get_formula_name(formula,known_molecules_dict)

    
    print(f"The total molar mass is: {molar_mass}" )
    print(f"the number of moles in the sample {number_of_moles:.5f}" )
    print(f"The formula name is: {formula_name}")

# Call main to start this program.
if __name__ == "__main__":
    main()